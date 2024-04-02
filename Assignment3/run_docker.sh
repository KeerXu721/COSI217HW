# Build Docker images
docker build -t spacy_api .
docker build -t streamlit_app .
docker build -t flask_server .

docker build -t sqlite_db .

# Run Docker containers
docker run -d -p 8000:8000 spacy_api
docker run -d -p 8501:8501 streamlit_app
docker run -d -p 5000:5000 --link sqlite_db flask_server
