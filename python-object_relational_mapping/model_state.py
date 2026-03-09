#!/usr/bin/python3
"""
    Module for creating an ORM model
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class State(Base):
    """
        The State Class for ORM
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
