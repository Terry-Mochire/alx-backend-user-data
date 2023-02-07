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
                                           base64_authorization_header: str) \
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
            return base64.b64decode(base64_authorization_header) \
                .decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str) \
            -> (str, str):

        """
        Returns the user email and password from the Base64 decoded value
        Args:
            decoded_base64_authorization_header: decoded string

        Returns:
            user email and password
        """
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) is not str:
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        return decoded_base64_authorization_header.split(':', 1)
