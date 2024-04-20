from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec
from huggingface_hub import hf_hub_download
from langchain.embeddings import HuggingFaceEmbeddings

index_name = "BSI-index"
load_dotenv()
PINECONE_KEY = os.getenv('PINECONE_KEY')

# load pdf data and split into chunks
loader = PyPDFLoader("./Data/BSI_all.pdf")
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(data)

# connect to pinecone and create index
pc = Pinecone(api_key=PINECONE_KEY)
pc.create_index(
    name=index_name,
    dimension=1536,
    metric="euclidean",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)
pinecone_index = pc.Index(index_name)

embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
pinecone_index.upsert(embeddings)




# docsearch=Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)
# query = 'Jakie przestępstwa są związane z bezpieczeństwem?'
# docs=docsearch.similarity_search(query)
# print(docs)