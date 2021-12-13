import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    log_in = Column(String(80), nullable= False)
    id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    email = Column(String(60), unique=True)
    favorites = relationship("Favorites")

class Favorites(Base):
    __tablename__= 'favorites'

    name = Column(String(200), nullable=True)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id= Column(Integer, ForeignKey('people.id'))
    planet_id= Column(Integer, ForeignKey('planet.id'))
    vehicle_id= Column(Integer, ForeignKey('vehicle.id'))

class People(Base):
    __tablename__= 'people'

    name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)
    age = Column(Integer, unique=True)
    favorites = relationship("Favorites")

class Planet(Base):
    __tablename__= 'planet'

    name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key=True)
    population= Column(Integer)
    favorites = relationship("Favorites")

class Vehicle(Base):
    __tablename__= 'vehicle'

    name = Column(String(100), nullable=False)
    id = Column(Integer, primary_key= True)
    speed = Column(Integer)
    favorites = relationship("Favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')