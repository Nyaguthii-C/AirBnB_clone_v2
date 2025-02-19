#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"))
    user_id = Column(String(60), ForeignKey("users.id"))
    text = Column(String(1024), nullable=False)
    place = relationship("Place", back_populates="reviews")
