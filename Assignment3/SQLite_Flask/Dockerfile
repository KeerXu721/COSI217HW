# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app_flask

# Copy the current directory contents into the container at /app
COPY . /app_flask

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install spacy && python -m spacy download en_core_web_sm

# Run the Flask application
CMD ["python", "app_flask.py"]
