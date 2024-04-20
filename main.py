import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_KEY = os.getenv('PINECONE_KEY')
print(PINECONE_KEY)