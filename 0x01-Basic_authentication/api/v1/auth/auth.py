#!/usr/bin/env python3
""" doc doc """
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """Authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns false"""
        return False

    def authorization_header(self, request=None) -> str:
        """returns None"""
        return None

    def current_user(self, requests=None) -> TypeVar('User'):
        """returns None"""
        return None
