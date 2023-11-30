# This line imports the SQLAlchemy class from the flask_sqlalchemy package.
#flask_sqlalchemy is a Flask extension that simplifies database integration with Flask applications.
from flask_sqlalchemy import SQLAlchemy


#this creates an instance of the SQLAlchemy class and assigns it to the variable db
#This  instance represents the database connection and provides methods and attrobutes to interact with the dB
db = SQLAlchemy()
