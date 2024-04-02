# Assignment 3 - Docker containers 🐳📦

This assignment is quite simple and straightforward, it will take the three elements: RESTful API, Streamlit application
and the Flask server with a SQLlite backend together and create a new code base using Docker. 

The Assignment3 folder contains three independent folders: RESTful_API, SQLite_Flask and streamlit_app. It also contains a docker-compos.yml
file which allows the user to access the three functionality simultaneously. 

There are two ways to run the Docker:
### Rune all three at once 🚀

To run the composer, type the following in your terminal:
```bash
docker-compose up
```
Then click [[http://localhost:5000]]([http://localhost:5000]) to access Flask server with SQLite backend; click [[http://localhost:8000]]([http://localhost:5000])
to access the RESTful API and click [[http://localhost:8501]]([http://localhost:8501]) to access the streamlit application. 

### Run them individually in their own directory

This is a little bit more complicated:

#### RESTful_API 🔗
```bash
cd RESTful_API
docker build -t my_fast_app .
docker run -d -p 8000:8000 my_fast_app
```
Then click [[http://localhost:8000]]([http://localhost:8000])

#### SQLite_Flask 🔑
```bash
cd SQLite_Flask
docker build -t my_flask_app . 
docker run -d  5000:5000 my_flask_app    
```
Then click [[http://localhost:5000]]([http://localhost:5000])

#### streamlit_app 🎬
```bash
cd streamlit_app
docker build -t my_streamlit_app .  
docker run -d -p 8501:8501 my_streamlit_app   
```
Then click [[http://localhost:8501]]([http://localhost:8501])