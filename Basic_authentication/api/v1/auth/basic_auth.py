#!/usr/bin/env python3
"""Basic Auth class"""
import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar

UserType = TypeVar('UserType')


class BasicAuth(Auth):
    """Basic authentication."""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Return the Base64 part of the Authorization header for Basic Auth."""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Return the decoded value of a Base64 string as UTF-8."""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> tuple:
        """Return (user_email, user_password) from decoded 'email:password'."""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email, password = decoded_base64_authorization_header.split(':', 1)
        return (email, password)

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> UserType:
        """Return the User instance for the given email and password."""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        user = User.search(user_email)
        if user is None:
            return None
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> UserType:
        """Overload Auth: retrieve the User instance for a request (Basic Auth)."""
        if request is None:
            return None
        header = self.authorization_header(request)
        if header is None:
            return None
        b64 = self.extract_base64_authorization_header(header)
        if b64 is None:
            return None
        decoded = self.decode_base64_authorization_header(b64)
        if decoded is None:
            return None
        email, password = self.extract_user_credentials(decoded)
        if email is None or password is None:
            return None
        return self.user_object_from_credentials(email, password)
