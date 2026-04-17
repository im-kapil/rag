from config import Config
from sentence_transformers import SentenceTransformer

def sentense_transformer_embedding_model():    
    return SentenceTransformer(model_name_or_path=Config.EMBEDDING_MODEL)