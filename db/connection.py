import os
from dotenv import load_dotenv
from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi

load_dotenv()

try:
    client = AsyncMongoClient(os.getenv('URI'), server_api=ServerApi('1'))

    print("Successfully connected to MongoDB!")

    db = client["storage-bot"]
    collections = db["collections"]
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    raise