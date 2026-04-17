from typing import Any
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embedding_model import sentense_transformer_embedding_model
from config import Config

class EmbeddingManager:
    def __init__(self):
        """
        Intialze tne embedding manager
        
        Args: 
            model_name: hugging face model for sentense enbedding
        """
        self.model = None
        self._load_model()
        
    def _load_model(self):
        """ Loader function to load the transformer Model """
        try: 
            print(f"Loading embedding model: {Config.EMBEDDING_MODEL}")
            self.model = sentense_transformer_embedding_model()
            print(f"Embedding model loaded successfully with dimenstions: {self.model.get_embedding_dimension()}")
        except Exception as e: 
            print(f"Failed to load model {Config.EMBEDDING_MODEL}", e)
            raise  
          
    def generate_embeddings(self, text: Any):
        if not self.model: 
            raise ValueError("Model is not loaded")
        print(f"generating embeddings for {len(text)} text")
        embeddings = self.model.encode(text, show_progress_bar=False)
        print(f"Generated embeddings with shape: {embeddings.shape}")
        return embeddings  
    
    def document_chunker(self, document_chunk: Any):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=0
            )
        return text_splitter.split_text(document_chunk)