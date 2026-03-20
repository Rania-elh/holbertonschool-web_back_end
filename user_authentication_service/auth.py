#!/usr/bin/env python3
"""Authentication helpers"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the password as bytes."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Return a string representation of a new UUID (module-private)."""
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
        """Return True if email exists and password matches the stored hash."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(
            password.encode("utf-8"),
            user.hashed_password.encode("utf-8"),
        )

    def create_session(self, email: str):
        """Create session UUID, persist it, return id or None."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str):
        """Return the User for this session_id, or None if missing/unknown."""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Clear the session_id for the given user."""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset token for the user; persist and return it."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update password using reset token; clear reset_token on success."""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed = _hash_password(password)
        self._db.update_user(
            user.id,
            hashed_password=hashed.decode("utf-8"),
            reset_token=None,
        )
