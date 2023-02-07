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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """
        Returns the decoded value of a Base64 string
        Args:
            base64_authorization_header: String to be decoded

        Returns:
            The decoded value of a Base64 string
        """
        import base64

        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None

        try:
            return base64.b64decode(base64_authorization_header)\
                .decode('utf-8')
        except Exception:
            return None
