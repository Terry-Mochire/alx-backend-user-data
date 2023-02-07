#!/usr/bin/env python3
"""
Class to manage the API authentication
"""
from typing import List, TypeVar

from flask import request


class Auth:
    """
    Auth class
    """

    def __int__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if a path should be authenticated
        Args:
            path:
            excluded_paths:

        Returns:

        """

        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns None
        Args:
            request:

        Returns:

        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None
        Args:
            request:

        Returns:

        """
        return None
