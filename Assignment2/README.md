# Assignment 2 - Flask SQLAlchemy🗄️

This assignment connects the flask website with a database backend using SQLAlchemy. 
There are three parts of the flask website:
1. A page to enter text to be processed. 
2. A page to show the results of processing, and store the results in the database.
3. A page to show the content of the database.

### Requirements 📋
```bash
pip install Flask Flask-SQLAlchemy
```

### How to run 👩‍💻
All the code is written in app_flask.py file. To run the code, simply run the *app_flask.py* file, and click the link: 
[[http://127.0.0.1:5000] ]([http://127.0.0.1:5000]), then you will be directed to the webpage. 

The main page will ask you to input a text. Then click "submit" to enter the text and see the result. 
On the second page, you will see results of processed data. 
Scroll down to the bottom of the page, there are two buttons: "back to form", which will direct you to the main (first) 
page; and "Go to table", which will direct you to the third page where you will see the content of the database. 

### Potential bugs 🪲
When I am running the code, sometimes it will raise "column not found" or "table not found" error. 
To fix this, try to delete the *instance* folder and restart the program. 