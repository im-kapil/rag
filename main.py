from query_helper import perform_search
from chroma_client import ChromaClient
from config import Config

def main():

    client = ChromaClient(persistent_directory_path=Config.CHROMA_DB_PATH)
    
    collection = client.get_collection(collection_name=Config.COLLECTION_NAME)
    
    queries = [
        "attention mechanism?"
        ]

    result = perform_search(collection=collection, query_texts=queries, results=10)
    
    print(":::::::::::::::::::::::::::: Queries result :::::::::::::::::::::::::::: \n ", result["documents"][0])

    # print(":::::::::::::::::::::::::::: Queries result :::::::::::::::::::::::::::: \n ", result)


if __name__ == "__main__":
    main()