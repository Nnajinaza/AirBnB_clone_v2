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
        name = ""

    @property
    def cities(self):
        """cities list
        """
        result = []
        for j, i in models.storage.all(models.city.City).items():
            if (i.state_id == self.id):
                result.append(i)
        return result
