from pymongo import MongoClient
import streamlit as st

def get_collection():
    username = st.secrets["mongo"]["username"]
    password = st.secrets["mongo"]["password"]
    host = st.secrets["mongo"]["host"]
    mongodb_uri = f"mongodb+srv://{username}:{password}@{host}/?retryWrites=true&w=majority&appName=Cluster0"
    cluster = MongoClient(mongodb_uri)
    db = cluster["linq_assessment_db"]
    collection = db["mock_data"]
    return collection

