#!/usr/bin/env python3
""" This is the basic Authentication implementation"""
from .auth import Auth
import base64
from models.user import User
from models.base import Base


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extracts the user credentials from the decodes dtring
        Return: two strings (user email and password ) seperated by a colon
        """

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # if the string do not contain the colon
        colon = ":"
        if colon not in decoded_base64_authorization_header:
            return None, None

        # split the decoded string at the colon point
        email_pass = decoded_base64_authorization_header.split(':')
        return email_pass[0], email_pass[1]

    Add the method def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ gets the user object from the credentials extracted from user
        - use the Search method from
        Return: user instance based on the password and email
        """
        # if both the password and usernames are not strings return None
        if not isinstance(user_email, str):
            return None
        if not isinstance(user_pwd, str):
            return None

        try:
            # search for the users from the dictionary file
            users = User.search({'email': user_email})
            # if its empty or email not exist, return None
            if not users or users == []:
                return None
            # check for the valid password
            for us in users:
                if us.is_valid_password(user_pwd):
                    return u
            return None
        except Exception:
            return None

