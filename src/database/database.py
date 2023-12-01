"""
Flask-SQLAlchemy Database Initialization

This code initializes a SQLAlchemy object ('db') for database integration in Flask using Flask-SQLAlchemy,
a Flask extension simplifying database interactions.

1. Import SQLAlchemy class from flask_sqlalchemy package, an extension for Flask applications.
2. Create an instance ('db') of the SQLAlchemy class to manage database connections and operations.

SQLAlchemy provides methods and attributes to interact with the database, including defining models,
performing CRUD operations, and managing database transactions in a Flask application.
"""
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy object for database management
db = SQLAlchemy()
