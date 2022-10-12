#!/usr/bin/python3
""" DBStorage """
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from os import getenv, environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base

"""Values retrieved by env variables"""
DATABASE = getenv("HBNB_MYSQL_DB")
USER = getenv("HBNB_MYSQL_USER")
PASSWORD = getenv("HBNB_MYSQL_PWD")
HOST = getenv("HBNB_MYSQL_HOST")
DATABASE_CONNECTION = (f'mysql+mysqldb://{USER}:{PASSWORD}@{HOST}/{DATABASE}')


class DBStorge():
    """ Private class attributes """
    __engine = None
    __session = None

    def __init__(self):
        """Create engine"""
        self.__engine = create_engine(DATEBASE_CONNECTION, pool_pre_ping=True)

        """Drop all tables if env variables HBNB_ENV
        is equal to test
        """
        env = getenv("HBNB_ENV")
        if (env == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the database session all objects
        """
        new_dict = {}
        if (cls is None):
            sessions = self.__session.query(cls).all()
            for value in sessions:
                key = __class.__name__ + '.' + value.id
                new_dict[key] = value
        return (new_dict)

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.query.add(obj)

    def save(self):
        """ Commit all changes of the current database """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj """
        if (obj is not None):
            self.__session.delete(obj)

    def reload(self):
        """ create the current database session
            (self.__session) from the engine
        """
        Base.metadata.create_all(engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.session = scoped_session(sess)
