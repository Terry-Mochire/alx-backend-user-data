#!/usr/bin/env python3
"""
Session Authentication
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Session Authentication Class
    """

    def __init__(self):
        self.user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Returns None
        Args:
            user_id:

        Returns:

        """
        if user_id is None or type(user_id) is not str:
            return None

        from uuid import uuid4
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
