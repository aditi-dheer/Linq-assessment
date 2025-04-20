from datastore_setup import get_collection
import random
from datetime import datetime
import time
import pytz

collection = get_collection()

def ingest_data():
    """Inserts mock temperature data into the database"""
    
    # get the latest id value to continue from the last one or start from 0
    if collection.count_documents({}) > 0:
        latest_entry = collection.find().sort('_id', -1).limit(1)
        id_number = latest_entry[0]['_id'] + 1

    else:
        id_number = 0

    # generate a random temperature value between 10 and 35
    temperature = random.randint(20, 25)

    # create a new post with id, city, temperature and timestamp
    post = {
        "_id": id_number,
        "city": "New York",
        "temperature": temperature,
        "timestamp": datetime.now(pytz.timezone("US/Eastern"))
    }
    id_number += 1

    # insert the new post into collection
    collection.insert_one(post)