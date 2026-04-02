""" Vectorstore module for document embedding and retrieval """

from typing import List
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document

from src import vectorstore

class VectorStore:
    """ Manages vectorstore application"""

    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = None
        self.retriever = None

    def create_retriever(self, documents: List[Document]):
        """ Create vectorstore from documents """
        self.vectorstore = FAISS.from_documents(documents, self.embeddings)
        self.retriever = self.vectorstore.as_retriever()

    def get_retriever(self):
        """ 
        Get retriever instance of vectorstore 

        Returns:
            retriever: Retriever instance of vectorstore
        """
        if self.retriever is None:
            raise ValueError("Vectorstore not initialized. Call create_retriever first.")
        return self.retriever