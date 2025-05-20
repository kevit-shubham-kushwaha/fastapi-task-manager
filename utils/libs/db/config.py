from pymongo import MongoClient
from utils.libs.config import (MONGODB_URI, MONGODB_DB, MONGODB_COLLECTION)
import sys

def connect_to_mongo(connection_string:str,db_name:str):
    try:
        client = MongoClient(connection_string)
        client.server_info()  # Trigger an exception if the connection fails
        print("MongoDB connection successful")
        return client[MONGODB_DB]
    except Exception as e:
        print(f"MongoDB connection failed: {e}")
        sys.exit(1)  # Exit the program if the connection fails


fast_api_db = connect_to_mongo(MONGODB_URI, MONGODB_DB)


fastapi_user_collection = fast_api_db[MONGODB_COLLECTION] 