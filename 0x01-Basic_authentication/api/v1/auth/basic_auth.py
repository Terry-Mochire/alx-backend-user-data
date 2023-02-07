#!/usr/bin/env python3
"""
Basic Auth Class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth Class
    """

    def __int__(self):
        pass

    def extract_base64_authorization_header(self, authorization_header: str) \
            -> str:
        """
        Returns the Base64 part of the Authorization header:
        Args:
            authorization_header:

        Returns:
            A string of Base64 encoded values
        """
        if authorization_header is None or \
                type(authorization_header) is not str:
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]
