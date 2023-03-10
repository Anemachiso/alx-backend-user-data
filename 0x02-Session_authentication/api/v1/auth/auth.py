#!/usr/bin/env python3
"""
API authentication module
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if API routes require authentication """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Checks if Authorization request header is present
        & contains values """
        if request is None or "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ placeholder """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""

        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")

        if SESSION_NAME is None:
            return None

        session_id = request.cookies.get(SESSION_NAME)

        return session_id
