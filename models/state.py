#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, DateTime, MetaData
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from os import environ, getenv

store_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    if (store_type == 'db'):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

    else:
        @property
        def cities():
            """ Returns the list of city if the id are the same """
            city_list = []
            for key, value in models.storage.all().items():
                if (value.state_id == state.id):
                    return (city_list.append(value))
            return city_list
