#!/usr/bin/env python3
""" doc doc doc """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """doc doc doc"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **criteria) -> User:
        """ Takes key-word args and returns first user that matches
            Args:
            **criteria (dict) -> dictionary of key-value pairs of items 
            we will use to search with
            Returns:
                User: The first user matvhing the provided criteria
            raises:
                InvalidRequestErro: if an invalid attribute is provided
                NoResultFound: if no user matches the search criteria

        """
        # make a query to the DB
        user_queried = self._session.query(User)
        # loop through the items to validate the items(optional)
        for key in criteria:
            if key not in User.__dict__:
                raise InvalidRequestError("Invalid attribute:{}".format(key))
        # confirmm that we are only searching for the first item
        if not user_queried.filter_by(**criteria).first:
            return NoResultFound
        # filer the items using the provided criteria
        for usr in user_queried.filter_by(**criteria):
            return usr

        raise NoResultFound
