#!/usr/bin/env python3
"""
SQLAlchemy model for a user.
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to the database
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# Create base class
Base = declarative_base()


class User(Base):
    """
    User model class.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, email, hashed_password,
                 session_id=None, reset_token=None):
        self.email = (email,)
        self.hashed_password = (hashed_password,)
        self.session_id = (session_id,)
        self.reset_token = reset_token
