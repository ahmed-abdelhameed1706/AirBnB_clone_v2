#!/usr/bin/python3
"""
DBStorage Engine Model to store the data
"""
from sqlalchemy import create_engine
import os
from models.base_model import Base, BaseModel
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


user = os.environ.get('HBNB_MYSQL_USER')
pwd = os.environ.get('HBNB_MYSQL_PWD')
host = os.environ.get('HBNB_MYSQL_HOST')
db = os.environ.get('HBNB_MYSQL_DB')

class DBStorage:
    """
    DB Storage to store the data
    """
    __engine = None
    __session = None
    
    def __init__(self):
        """
        Initialize the DB Storage
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                        format(user, pwd, host, db),
                                        pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """
        query on the current database session
        """
        new_dict = {}
        classes = [City, Review, User, Amenity, State, Place]
        if cls is None:
            for clss in classes:
                
                objs = self.__session.query(clss).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        elif cls in classes:
            
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        """Adds object to current db session"""
        self.__session.add(obj)
        
    def save(self):
        """Commits all changes"""
        self.__session.commit()
        
    def delete(self, obj=None):
        """Deletes from current database session if obj is not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()
    
    def reload(self):
        """Creates all tables in database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
