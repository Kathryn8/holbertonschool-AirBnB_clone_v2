#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
#from models import storage


class State(BaseModel, Base):
    """Class definition for the state class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", back_populates="state", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """returns the list of City instance that belong to that State"""
        all_cities_dict = storage.all(City)
        return_list = []
        for key, value in all_cities_dict.items():
            if self.id == value.state_id:
                return_list.append(value)
        return return_list
