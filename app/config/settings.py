from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

QDRANT_PATH = os.getenv("QDRANT_PATH")

COLLECTION_NAME = os.getenv("COLLECTION_NAME")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

LLM_MODEL = os.getenv("LLM_MODEL")

TOP_K = int(os.getenv("TOP_K",5))