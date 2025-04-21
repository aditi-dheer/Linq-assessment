# 📥 Data Ingestion

## Overview

This script (`data_ingest.py`) generates **mock weather data** and inserts it into a **MongoDB** collection. The data simulates temperature readings for New York City, including a timestamp and a unique ID for each entry. This script is designed to demonstrate real-time data ingestion into a datastore.

---

## 🔧 How It Works

1. **Connect to the Datastore**  
   The script uses the `get_collection()` function from `datastore_setup.py` to connect to the appropriate MongoDB collection.

2. **Determine the Next ID**  
   It checks if any documents already exist in the collection:
   - If they do, it finds the latest entry and increments the ID.
   - If not, it starts from ID `0`.

3. **Generate Random Data**  
   A random temperature between **20°C and 25°C** is generated using Python’s `random.randint()`.

4. **Create a New Document**  
   The document includes:
   - `_id`: A unique integer identifier.
   - `city`: Always set to `"New York"`.
   - `temperature`: The generated random temperature.
   - `timestamp`: The current date and time in US/Eastern timezone.

5. **Insert the Document**  
   The script then inserts this document into the MongoDB collection using `insert_one()`.
