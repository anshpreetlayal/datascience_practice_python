"""defines a Company class that represents a company model in a database using SQLAlchemy, a popular Object-Relational Mapping (ORM) library for Python"""
from src.database.database import db   #This line imports the DB object from the givemm module. the db object is an instance of SQLAlchemy's SQLAlchemy class and represents the DB
class Company(db.Model):

    """
    Represents a company.

    Attributes:
        company_id (int): The unique identifier for the company.
        name (str): The name of the company.

    """

    __tablename__ = "company"

    company_id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(255))
    #user_company_mapping = db.relationship('UserCompanyMapping', backref='company', lazy=True) 
