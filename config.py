import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    CHROMA_DB_PATH: str = os.getenv("CHROMA_DB_PATH", "./chroma_db")
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME", "default_collection")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    PDF_PATH: str = os.getenv("PDF_PATH")