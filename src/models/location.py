#from src.database.database import db: This line imports the db object, which is an instance of SQLAlchemy, used for defining the database model.
from src.database.database import db
#Defines a SQLAlchemy model named Location that inherits from db.Model, indicating it's a model class mapped to a database table.
class Location(db.Model):

    """
    Represents a location.

    Attributes:
        location_id (int): The unique identifier for the location.
        city (str): The city of the location.
        state (str): The state of the location.
        country (str): The country of the location.
    """

    __tablename__ = "location"

    location_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    country = db.Column(db.String(255))
    # Add other location-related fields as needed

    # Other methods as needed
