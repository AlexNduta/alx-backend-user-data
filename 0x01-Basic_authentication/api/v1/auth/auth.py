#!/usr/bin/env python3
""" doc doc """
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns false
        """
        if path is None: # if the path does not exist, authenticate
            return True
        # if there are no excluded paths, auth is required
        if not excluded_paths:
            return True
        # check if path ends with '/' else apend
        normalized_path = path if path.endswith('/') else path + '/'

        # check if normalized path is in the list of exluded paths
        for ex_path in excluded_paths:
            if ex_path.endswith and normalized_path == ex_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """returns None"""
        # if no requets is provided, return None
        if request is None:
            return None
        # If Authorization is not in the request headers return Null
        if 'Authorization' is not request.headers:
            return None
        # return the value of the authorisation
        return request.headers.get('Authorization')

    def current_user(self, requests=None) -> TypeVar('User'):
        """returns None"""
        return None
