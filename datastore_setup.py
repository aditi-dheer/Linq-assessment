from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_collection():

    mongodb_uri = os.getenv("MONGODB_URI")
    cluster = MongoClient(mongodb_uri)
    db = cluster["linq_assessment_db"]
    collection = db["mock_data"]
    return collection

