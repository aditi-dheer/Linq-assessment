FROM python
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
COPY .env /app/.env
EXPOSE 8501
CMD ["streamlit", "run", "visualization.py"]