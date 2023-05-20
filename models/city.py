#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.state import State
from sqlalchemy.orm import relationship
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The class contains attributes

    Args:
        __tablename: represents the table
        name: represents a satring
        state_id: foreign key to state_id
    """
    if (storage_engine == "db"):
        __tablename__ = 'cities'
        state_id = Column(String(128), ForeignKey('state.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""
