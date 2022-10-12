#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, MetaData
from sqlalchemy import Integer, ForeignKey


class City(BaseModel, Base):
    """ The class contains attributes

    Args:
        __tablename: represents the table
        name: represents a satring
        state_id: foreign key to state_id
    """
    __tablename__ = 'cities'
    state_id = Column(String(128), ForeignKey('state.id'), nullable=False)
    name = Column(String(128), nullable=False)
