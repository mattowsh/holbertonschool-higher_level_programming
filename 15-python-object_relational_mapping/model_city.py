#!/usr/bin/python3
"""
Task 14: python file that contains the class definition of a City and
an instance Base = declarative_base()
"""

import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ New class to generate a table """

    __tablename__ = "cities"
    # Defines new class attributes:
    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
