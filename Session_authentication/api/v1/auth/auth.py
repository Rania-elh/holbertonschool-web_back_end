#!/usr/bin/env python3
"""Auth class"""
from os import getenv
from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    """Template for all authentication system."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return True if path is not in excluded_paths, False otherwise.
        Slash tolerant: /api/v1/status and /api/v1/status/ match the same.
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        path = path if path.endswith('/') else path + '/'
        for excluded in excluded_paths:
            ex = excluded if excluded.endswith('/') else excluded + '/'
            if path == ex:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return the value of the Authorization header or None."""
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """Return None - request will be the Flask request object."""
        return None

    def session_cookie(self, request=None):
        """Return the value of the session cookie (name from SESSION_NAME env)."""
        if request is None:
            return None
        cookie_name = getenv("SESSION_NAME")
        if cookie_name is None:
            return None
        return request.cookies.get(cookie_name)
