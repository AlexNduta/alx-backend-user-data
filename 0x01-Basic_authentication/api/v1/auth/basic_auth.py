#!/usr/bin/env python3
""" This is the basic Authentication implementation"""
from .auth import Auth


class BasicAuth(Auth):
    """ empty for now"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the Base64 auth header
        -authorization_header: 'Authorisation' key in header
        """

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        starter = authorization_header.startswith('Basic ')
        if starter is False:
            return None

        after_basic = authorization_header[6:]
        return after_basic
