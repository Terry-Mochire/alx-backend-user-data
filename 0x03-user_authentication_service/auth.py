#!/usr/bin/env python3

"""
Authenticates a user.
"""

import bcrypt


def _hash_password(password: str) -> str:
    """
    Hashes a password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
