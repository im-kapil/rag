from typing import Any
from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader:
    """
    A utility class for loading documents using LangChain's document_loaders.

    This class provides a simple interface to load document files from a given
    file path or URL and convert them into a list of LangChain Document objects.
    Each Document contains extracted text (`page_content`) along with metadata
    such as page number, source, and other PDF attributes.

    Typical use case:
        - Load documents for preprocessing
        - Chunk text for embedding generation
        - Use in RAG (Retrieval-Augmented Generation) pipelines
    """

    def __init__(self):
        """
        Initialize the DocumentLoader.

        Currently, no parameters are required. This class acts as a thin wrapper
        around document_loader.
        """
        pass
    
    def load_pdf(self, pdf_url: str) -> list[dict, Any]:
        """
        Load a PDF file and return its contents as a list of Document objects.

        Args:
            pdf_url (str): Path or URL to the PDF file to be loaded.

        Returns:
            list: A list of LangChain Document objects, where each Document
                  represents a page (or segment) of the PDF and contains:
                  - page_content (str): Extracted text
                  - metadata (dict): Information such as page number, source, etc.

        Raises:
            Exception: If the PDF cannot be loaded or parsed.

        Example:
            >>> loader = DocumentLoader()
            >>> docs = loader.load_pdf("https://example.com/sample.pdf")
            >>> print(docs[0].page_content)
        """
        try:
            print("PDF loading.. 🚀 ")
            loader = PyPDFLoader(pdf_url)
            document = loader.load()
            print("PDF Loaded successfully.. 😇 ")
  
            return document
        except Exception as e: 
            print(f"Encountered error while loading pdf: {pdf_url}", e)
            
        return e    