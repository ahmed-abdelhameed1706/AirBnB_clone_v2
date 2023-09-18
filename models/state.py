#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    
    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances with
        state_id equals to the current State.id
        """
        from models import storage
        from models.city import City
        city_list = []
        _cities = storage.all(City).values()
        for city in _cities:
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
        
        
