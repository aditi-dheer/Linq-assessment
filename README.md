# 🌤 Temperature Tracker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>

</p>

🔗 **Access the Streamlit Dashboard Here**: [NYC Temperature Tracker on Streamlit](https://aditi-dheer-temperature-dashboard-visualization-98ddjs.streamlit.app/)

A dynamic Streamlit dashboard that simulates real-time temperature tracking in New York City using randomly generated mock data. The project demonstrates how to simulate real-time data ingestion, storage, and visualization using modern backend tools.

## 🧠 Project Overview

This application mimics real-time weather updates by generating random temperature values at regular intervals and storing them in a MongoDB database. The Streamlit dashboard refreshes every 10 seconds to reflect new data, giving users a live look at changing temperature trends over time.

It serves as a lightweight prototype for real-world systems that need to track and visualize time-series data.

## 🛠 Tech Stack

| Tool           | Purpose                                |
|----------------|----------------------------------------|
| Python         | Core programming language              |
| Streamlit      | Interactive data visualization         |
| MongoDB        | NoSQL database for storing temperature |
| pymongo        | MongoDB driver for Python              |
| random         | Random number generation for sample data |
| datetime       | Timestamping each entry                |

## 💡 Key Features  

Real-time style dashboard with automatic refresh  

Simulates live temperature data without relying on an API  

Timestamped entries saved in MongoDB  

Line chart visualization of temperature trends  

Modular, clean codebase for easy extension  

