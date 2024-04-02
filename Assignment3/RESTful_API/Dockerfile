# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app_fastapi

# Copy the current directory contents into the container at /app
COPY . /app_fastapi

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir fastapi uvicorn

RUN pip install spacy && python -m spacy download en_core_web_sm

EXPOSE 8000

# Run the Flask application
# CMD ["uvicorn", "app_fastapi:app --reload"]
CMD ["uvicorn", "app_fastapi:app", "--reload"]
