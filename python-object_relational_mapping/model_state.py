#!/usr/bin/python3
"""
Task 6: python file that contains the class definition of a State and
an instance Base = declarative_base()
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ New class to generate a table """

    __tablename__ = "states"
    # Defines new class attributes:
    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
