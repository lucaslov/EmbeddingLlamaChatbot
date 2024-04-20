import os
from dotenv import load_dotenv
from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

PINECONE_KEY = os.getenv('PINECONE_KEY')
loader = PyPDFLoader("../data/summary_strategy.pdf")
data = loader.load()
print (f'You have {len(data)} document(s) in your data')
print (f'There are {len(data[0].page_content)} characters in your document')