#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Integer, DateTime, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Table
from models.amenity import Amenity
from models.review import Review

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id",
           String(60),
           ForeignKey("places.id"),
           primary_key=True,
           nullable=False
    ),
    Column("amenity_id",
           String(60),
           ForeignKey("amenities.id"),
           primary_key=True,
           nullable=False
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer(), default=0, nullable=False)
    number_bathrooms = Column(Integer(), default=0, nullable=False)
    max_guest = Column(Integer(), default=0, nullable=False)
    price_by_night = Column(Integer(), default=0, nullable=False)
    latitude = Column(Float(), nullable=True)
    longitude = Column(Float(), nullable=True)
    amenity_ids = []
    user = relationship("User") # is this correct?
    cities = relationship("City") # is this correct?
    reviews = relationship(
        "Review", back_populates="place",
        cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    # maybe add to above line: back_populates="places"?? plural?

    @property
    def reviews(self):
        """Return list of Review instances, place_id equals current Place.id"""
        from models import storage
        review_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """returns the list of Amenity instances based on the attribute amenity_ids"""
        amenity_obj_list = []
        from models import storage
        for amenity in storage.all(Amenity).values():
            if amenity.id == self.amenity_ids:
                amenity__obj_list.append(amenity)
        return amenity_obj_list

    @amenities.setter
    def amenities(self, obj):
        """that handles append method for adding an Amenity.id"""
        if obj is not type(Amenity):
            return
        self.amenity_ids.append(obj.id)
