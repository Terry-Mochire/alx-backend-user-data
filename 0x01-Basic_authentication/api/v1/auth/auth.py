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

        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/' and path[-1] != '*':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/' and excluded_path[-1] != '*':
                excluded_path += '/'

            if excluded_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns None
        Args:
            request:

        Returns:

        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns None
        Args:
            request:

        Returns:

        """
        return None
