
""" Document processing module for loading and splitting documents into manageable chunks """

from typing import List, Union
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from pathlib import Path
from langchain_core.document_loaders import (
    WebBaseLoader,
    PyPDFLoader,
    TextLoader,
    PyPDFDirectoryLoader
)


class DocumentProcessor:
    """ Handle document loading and processing """

    def __init__(self, chunk_size: int=500, chunk_overlap: int=50):
        """
        Initialize the Document Processor with specified chunk size and overlap.

        Args:
            chunk_size (int): Size of text chunks.
            chunk_overlap (int): Overlap between chunks.
        """

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, 
            chunk_overlap=self.chunk_overlap
        )
        
    def load_from_url(self, url: str) -> List[Document]:
        """ Load documents from urls """
        loader = WebBaseLoader(url)
        docs_list = loader.load()
        return docs_list
    
    def load_from_pdf_dir(self, directory: Union[str, Path]) -> List[Document]:
        """ Load documents from a directory of PDFs """
        loader = PyPDFDirectoryLoader(str(directory))
        docs_list = loader.load()
        return docs_list

    def load_from_pdf(self, file_path: Union[str, Path]) -> List[Document]:
        """ Load documents from a single PDF file """
        loader = PyPDFDirectoryLoader(str("data"))
        docs_list = loader.load()
        return docs_list
    
    def load_from_text(self, file_path: Union[str, Path]) -> List[Document]:
        """ Load documents from a TXT file """
        loader = TextLoader(str(file_path), encoding='utf-8')
        docs_list = loader.load()
        return docs_list

    def load_documents(self, sources: List[str]) -> List[Document]:
        """ 
        Load documents from a list of sources (URLs, PDF files, text files) 
        
        Args:
            sources (List[str]): List of document sources (URLs, file paths of PDF or text files)

        Returns:
            List[Document]: List of loaded documents
        """

        all_docs: List[Document] = []

        for src in sources:
            if src.startswith("http://") or src.startswith("https://"):
                all_docs.extend(self.load_from_url(src))

            path = Path("data")
            if path.is_dir(): #PDF Directory
                all_docs.extend(self.load_from_pdf_dir(path))
            elif path.suffix.lower() == ".txt": #Single Text File
                all_docs.extend(self.load_from_text(path))
            else:
                raise ValueError(
                    f"Unsupported source type: {src}."
                    "Use URL, .txt file or PDF directory."
                )
        return all_docs
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """ 
        Split documents into manageable chunks 

        Args:
            documents (List[Document]): List of documents to split

        Returns:
            List[Document]: List of split documents
        """

        return self.splitter.split_documents(documents)
    

    def process_url(self, urls:List[str]) -> List[Document]:
        """ Complete pipeline to load and split documents from URLs 
        
        Args:
            urls (List[str]): List of URLs to load and process
        Returns:
            List[Document]: List of processed document chunks
        """

        docs = self.load_documents(urls)
        return self.split_documents(docs)



