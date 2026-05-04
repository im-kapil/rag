import chromadb
import logging
from typing import List, Optional, Dict, Any
from chromadb.api import ClientAPI
from chromadb.api.models.Collection import Collection
from embedding_model import sentense_transformer_embedding_model

logger = logging.getLogger(__name__)

class ChromaClient:
    def __init__(self, persistent_directory_path: str):
        try:
            print("Initializing Chroma client")
            self.client: ClientAPI = chromadb.PersistentClient(persistent_directory_path)
            print("Chroma client initialized successfully")
        except Exception as e:
            print("Failed to initialize Chroma client")
            raise RuntimeError("Chroma client initialization failed") from e

    def create_collection(self, collection_name: str, metadata: Optional[Dict[str, Any]] = None) -> Collection:
        try:
            logger.info(f"Creating collection: {collection_name}")
            return self.client.create_collection(
                name=collection_name, 
                embedding_function=sentense_transformer_embedding_model(),
                metadata=metadata
                )
        except Exception as e:
            logger.exception(f"Failed to create collection: {collection_name}")
            raise

    def get_or_create_collection(self, collection_name: str, metadata: Optional[Dict[str, Any]] = None) -> Collection:
        try:
            print(f"Getting or creating collection: {collection_name}")
            return self.client.get_or_create_collection(
                name=collection_name, 
                metadata=metadata
                )
        except Exception as e:
            print(f"Failed to get/create collection: {collection_name}")
            raise

    def list_collections(self):
        try:
            logger.info("Listing collections")
            return self.client.list_collections()
        except Exception as e:
            logger.exception("Failed to list collections")
            raise

    def get_collection(self, collection_name: str) -> Collection:
        try:
            logger.info(f"Fetching collection: {collection_name}")
            return self.client.get_collection(collection_name)
        except Exception as e:
            logger.exception(f"Failed to fetch collection: {collection_name}")
            raise

    def peek_collection(self, collection: Collection, limit: int = 10):
        try:
            logger.info(f"Peeking into collection, limit={limit}")
            return collection.peek(limit)
        except Exception as e:
            logger.exception("Failed to peek collection")
            raise

    def add_data_to_collection(
        self,
        collection: Collection,
        ids: List[str],
        embeddings: List[List[float]],
        documents: List[str],
        metadatas: Optional[List[Dict[str, Any]]] = None
    ):
        try:
            if not len(ids) or not len(embeddings) or not len(documents):
                raise ValueError("ids, embeddings, and documents cannot be empty")

            if not (len(ids) == len(embeddings) == len(documents)):
                raise ValueError("ids, embeddings, and documents must have same length")

            if metadatas and len(metadatas) != len(ids):
                raise ValueError("metadatas length must match ids")

            logger.info(f"Adding {len(ids)} records to collection")

            return collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas
            )

        except Exception as e:
            logger.exception("Failed to add data to collection")
            raise