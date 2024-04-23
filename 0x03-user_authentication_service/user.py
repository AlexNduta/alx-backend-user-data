#!/usr/bin/env python3
"""model `Users` for table `users`
Columns
id- integer primary key
email: a non-nullable string
hashed_password : a non-nullable string
session_id : nullable string
reset_token : nullable string
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """ represents our database """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String)
    reset_token = Column(String)
