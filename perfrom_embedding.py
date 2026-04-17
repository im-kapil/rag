from embedding_manager import EmbeddingManager
from document_loader import DocumentLoader
from chroma_client import ChromaClient
from config import Config

def load_pdf(pdf_path: str): 
    document_loader = DocumentLoader()
    return document_loader.load_pdf(pdf_path)

def load_embedding_manager():
    return EmbeddingManager()

def load_chroma_client(db_path: str):
    return ChromaClient(db_path)

embedding_manager = load_embedding_manager()

chroma_client = load_chroma_client(Config.CHROMA_DB_PATH)

collection = chroma_client.get_or_create_collection(Config.COLLECTION_NAME)

document = load_pdf(Config.PDF_PATH)

# Chunk the document
text_chunks = []
embeddings = []
for item in document:
    chunks = embedding_manager.document_chunker(item.page_content)
    item = {
        "text": chunks,
        "metas": item.metadata
    }
    text_chunks.append(item)
   
# Generate embeddings for documents chunks
for chunk in text_chunks:
    embeddings.append(embedding_manager.generate_embeddings(chunk["text"]))

for i in range(0, len(text_chunks)):
    dynamic_ids = []

    for j in range(0, len(text_chunks[i]['text'])):
        dynamic_ids.append(f"{j}")

    if len(embeddings[i]) and len(text_chunks[i]['text']) and len(dynamic_ids):
        chroma_client.add_data_to_collection(
            collection,
            dynamic_ids,
            embeddings[i],
            text_chunks[i]['text'],
            # [{"chapter": 3, "verse": 16}, {"chapter": 3, "verse": 5}, {"chapter": 29, "verse": 11}],
        )
        
        dynamic_ids.clear()
        print("Added data to collection")