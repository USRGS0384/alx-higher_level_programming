#!/usr/bin/python3
"""Lists states"""

from relationship_state import base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative base

class City(Base):
    """Class that name the city"""
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, nulltable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
