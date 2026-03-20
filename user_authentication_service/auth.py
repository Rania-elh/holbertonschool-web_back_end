#!/usr/bin/env python3
"""Authentication helpers
"""
import uuid
from typing import Optional

import bcrypt
from sqlalchemy.exc import NoResultFound

from db import DB
from user import User

__all__ = ["Auth"]


def _hash_password(password: str) -> bytes:
    """Hash password with bcrypt.hashpw and bcrypt.gensalt; return bytes."""
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt)


def _generate_uuid() -> str:
    """Return str(uuid.uuid4()) using the uuid module.

    Private to this module; must not be imported or used outside auth.py.
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Create a new user or raise ValueError if email already exists."""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            pass
        else:
            raise ValueError(
                "User {} already exists".format(email)
            )
        hashed = _hash_password(password)
        return self._db.add_user(
            email, hashed_password=hashed.decode("utf-8")
        )

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login: find user by email, then bcrypt.checkpw.

        Locate the user by email. If found, compare password with
        bcrypt.checkpw. Return True only when the password matches;
        otherwise return False (unknown user, wrong password, or error).
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        pwd_bytes = password.encode("utf-8")
        hash_bytes = user.hashed_password.encode("utf-8")
        try:
            return bcrypt.checkpw(pwd_bytes, hash_bytes)
        except ValueError:
            return False

    def create_session(self, email: str) -> Optional[str]:
        """Find user by email, set session_id to a new UUID, return it.

        Uses self._db.find_user_by, _generate_uuid, and self._db.update_user
        only. Returns None if no user exists for the email.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        new_session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=new_session_id)
        return new_session_id

    def get_user_from_session_id(
        self, session_id: Optional[str]
    ) -> Optional[User]:
        """Return the User for this session_id, or None.

        If session_id is None or no row matches, return None. Otherwise use
        self._db.find_user_by(session_id=...) and return the User.
        """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Set the user's session_id to None via self._db.update_user.

        Persists session_id=None for the row identified by user_id. Returns
        None.
        """
        self._db.update_user(user_id=user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """Find user by email; set reset_token to a new UUID; return token str.

        If no user matches the email, raise ValueError. Uses _generate_uuid and
        self._db.find_user_by / self._db.update_user.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError(
                "User with email {} not found".format(email)
            )
        token = _generate_uuid()
        self._db.update_user(user_id=user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """Find user by reset_token; set hashed_password and reset_token=None.

        If no user matches the token, raise ValueError. Otherwise hash the
        password with _hash_password and persist via self._db.update_user.
        Returns None.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError(
                "Invalid reset token {}".format(reset_token)
            )
        hashed = _hash_password(password)
        self._db.update_user(
            user_id=user.id,
            hashed_password=hashed.decode("utf-8"),
            reset_token=None,
        )
        return None
