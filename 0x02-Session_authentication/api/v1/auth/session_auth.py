#!/usr/bin/env python3
"""
Session Authentication
"""

from api.v1.auth.auth import Auth
from models.user import User


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
        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns None
        Args:
            session_id:

        Returns:

        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """

        :param request:
        :return:
        """

        user_id = self.user_id_for_session_id(self.session_cookie(request))
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """

        :param request:
        :return:
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        print(session_id)
        if session_id is None:
            return False
        if self.user_id_for_session_id(session_id) is None:
            return False
        else:
            del self.user_id_by_session_id[session_id]
            return True
