#!/usr/bin/env python3
"""User model"""
from models.base import Base
import json
import os
import uuid


class User(Base):
    """User model - storage via file serialization"""

    __file_path = "User.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        """Initialize user"""
        super().__init__(*args, **kwargs)
        self.id = str(uuid.uuid4()) if not kwargs.get('id') else kwargs['id']
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')

    def to_dict(self):
        """Return dict representation (without password for safety)"""
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    def display_name(self):
        """Return display name (first_name last_name)"""
        return "{} {}".format(self.first_name, self.last_name).strip()

    def is_valid_password(self, pwd: str) -> bool:
        """Return True if pwd is the password of this user"""
        if pwd is None:
            return False
        return pwd == self.password

    def save(self):
        """Save this user to the file (create or update)"""
        objects = {}
        if os.path.exists(self.__class__.__file_path):
            try:
                with open(self.__class__.__file_path, 'r', encoding='utf-8') as f:
                    objects = json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        objects[self.id] = {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        self.__class__._save_objects(objects)

    @classmethod
    def _get_objects(cls):
        """Get all user objects from file"""
        if os.path.exists(cls.__file_path):
            try:
                with open(cls.__file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data
            except (json.JSONDecodeError, IOError):
                return {}
        return {}

    @classmethod
    def _save_objects(cls, objects):
        """Save user objects to file"""
        with open(cls.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objects, f, indent=2)
        cls.__objects = objects

    @classmethod
    def count(cls):
        """Return the number of users"""
        return len(cls.all())

    @classmethod
    def all(cls):
        """Return list of all User instances"""
        objects = {}
        if os.path.exists(cls.__file_path):
            try:
                with open(cls.__file_path, 'r', encoding='utf-8') as f:
                    objects = json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return [User(**v) for v in objects.values()]

    @classmethod
    def get(cls, user_id):
        """Get user by id"""
        for user in cls.all():
            if user.id == user_id:
                return user
        return None

    @classmethod
    def create(cls, **kwargs):
        """Create and save a new user"""
        user = cls(**kwargs)
        objects = {}
        if os.path.exists(cls.__file_path):
            try:
                with open(cls.__file_path, 'r', encoding='utf-8') as f:
                    objects = json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        objects[user.id] = {
            'id': user.id,
            'email': user.email,
            'password': user.password,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        cls._save_objects(objects)
        return user

    @classmethod
    def update(cls, user_id, **kwargs):
        """Update user by id"""
        user = cls.get(user_id)
        if not user:
            return None
        if 'first_name' in kwargs:
            user.first_name = kwargs['first_name']
        if 'last_name' in kwargs:
            user.last_name = kwargs['last_name']
        objects = {}
        if os.path.exists(cls.__file_path):
            try:
                with open(cls.__file_path, 'r', encoding='utf-8') as f:
                    objects = json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        if user.id in objects:
            objects[user.id]['first_name'] = user.first_name
            objects[user.id]['last_name'] = user.last_name
            cls._save_objects(objects)
        return user

    @classmethod
    def remove(cls, user_id):
        """Remove user by id"""
        user = cls.get(user_id)
        if not user:
            return None
        objects = {}
        if os.path.exists(cls.__file_path):
            try:
                with open(cls.__file_path, 'r', encoding='utf-8') as f:
                    objects = json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        objects.pop(user.id, None)
        cls._save_objects(objects)
        return user

    @classmethod
    def find_by(cls, **kwargs):
        """Find user by attributes (e.g. email=...)"""
        for user in cls.all():
            match = all(getattr(user, k) == v for k, v in kwargs.items())
            if match:
                return user
        return None

    @classmethod
    def search(cls, email: str):
        """Lookup user by email (class method for Basic Auth)"""
        return cls.find_by(email=email)
