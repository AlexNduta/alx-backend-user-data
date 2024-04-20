#!/usr/bin/env python3
""" This is the basic Authentication implementation"""
from .auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decodes the base64_authorization_header
        Args: base64_authorization_header: a decoded string got from the header
        Returns: a decoded string as a UTF-8 or none  if the header is invalid
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # decode the base64 string
            decoded_str = base64.b64decode(base64_authorization_header)
            # return decoded bytes as utf-8 string
            return decoded_str.decode('utf-8')
        except Exception:
            # the exception handled(invalid base 64)
            return None
