# Dockerfile for Streamlit application
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install spacy && python -m spacy download en_core_web_sm

COPY . .

CMD ["streamlit", "run", "app.py"]


