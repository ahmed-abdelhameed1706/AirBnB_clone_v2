#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
import os
from sqlalchemy.orm import relationship


db_type = os.environ.get('HBNB_TYPE_STORAGE')


place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True),
        )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship(
        'Review', backref='place', cascade='all, delete')
    amenities = relationship(
            'Amenity', secondary=place_amenity,
            viewonly=False)
    
    if db_type != 'db':
        @property
        def reviews(self):
            """
            getter for reviews for file storage
            """
            from models import storage
            from models.review import Review
            reviews_list = []
            _reviews = storage.all(Review).values()
            for review in _reviews:
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities_prop(self):
            """
            getter for the aminites
            """
            from models import storage
            from models.amenity import Amenity
            amenities_list = []
            _amenities = storage.all(Amenity).values()
            for amenity in _amenities:
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities_prop.setter
        def amenities_prop(self, obj):
            """
            setter for the amenintes
            """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
