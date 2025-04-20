import time
import pandas as pd
import plotly.express as px
import streamlit as st
from datastore_setup import get_collection
from data_ingest import ingest_data

# retrieve collection to access data
collection = get_collection()

# streamlit setup
st.set_page_config(
    page_title="NYC Temperature Updates",
    page_icon="🌦️",
    layout="wide",
)

st.title("Real-Time NYC Temperature Updates")
placeholder = st.empty()

# loop to update the data every 5 seconds
for seconds in range(2000):

    # calls the function to ingest new data
    ingest_data()

    # query last 10 records from database
    cursor = collection.find().sort("_id", -1).limit(10)
    data = list(cursor)

    # create and display the plot
    if data:
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        fig = px.line(df, x='timestamp', y='temperature', title='Temperature Over Time', markers=True)
        fig.update_layout(yaxis_title="°C", xaxis_title="Timestamp")

        with placeholder.container():
            st.plotly_chart(fig, use_container_width=True, key=f"temperature_chart_{seconds}")
    else:
        st.write("No data available yet.")

    # refresh every 5 seconds for real-time functionality
    time.sleep(5)