"""defines a Company class that represents a company model in a database using SQLAlchemy, a popular Object-Relational Mapping (ORM) library for Python"""
from src.database.database import db   #This line imports the DB object from the givemm module. the db object is an instance of SQLAlchemy's SQLAlchemy class and represents the DB
class Company(db.Model): #the Company class that inherits from db.Model, which is a base class provided by SQLAlchemy for database models.

    """
    Represents a company.

    Attributes:
        company_id (int): The unique identifier for the company.
        name (str): The name of the company.

    """

    __tablename__ = "company"  #Specifies the name of the database table associated with this model. In this case, it's named "company"

    company_id = db.Column(db.Integer, primary_key=True)  #Defines a column named company_id of type Integer in the "company" table. It serves as the primary key for uniquely identifying each company.
    name = db.Column(db.String(255)) #Defines a column named name of type String(255) in the "company" table to store the name of the company.
    #user_company_mapping = db.relationship('UserCompanyMapping', backref='company', lazy=True)  #This line is commented out, but it suggests that there might be a relationship defined between the Company model
    # and a UserCompanyMapping model. SQLAlchemy provides a way to establish relationships between models using relationship to represent the association between different tables/entities.


    #Summary: Company class is a SQLAlchemy model representing a company entity in the database. It contains attributes (company_id and name) that map to columns in the "company" table.
    # If uncommented and properly configured, the relationship attribute could establish a link between Company and UserCompanyMapping models, defining a relationship between the two tables/entities in the database.
