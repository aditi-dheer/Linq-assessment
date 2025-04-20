FROM python
WORKDIR /app
COPY . .
COPY .streamlit /root/.streamlit
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "visualization.py"]