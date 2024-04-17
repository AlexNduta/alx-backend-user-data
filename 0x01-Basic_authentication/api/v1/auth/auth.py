#!/usr/bin/env python3
""" doc doc """
from flask import request
import typing


class Auth:
    """Authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns false"""
        return False

    def authorization_header(self, request=None) -> str:
        """returns None"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, requests=None) -> TypeVar('User'):
        """returns None"""
        if request is None:
            return None
        return None
