#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """
    model to represent aminty class
    """
    __tablename__ = 'amenities'
    name = ""
