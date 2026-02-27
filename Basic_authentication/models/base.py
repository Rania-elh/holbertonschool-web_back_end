#!/usr/bin/env python3
"""Base model - handle serialization to file"""
import json
import os


class Base:
    """Base class for all models - serialization/deserialization in files"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        """Initialize instance"""
        pass

    @classmethod
    def load_from_file(cls):
        """Load objects from file"""
        if os.path.exists(cls.__file_path):
            try:
                with open(cls.__file_path, 'r', encoding='utf-8') as f:
                    cls.__objects = json.load(f)
            except (json.JSONDecodeError, IOError):
                cls.__objects = {}
        else:
            cls.__objects = {}

    @classmethod
    def save_to_file(cls, objects):
        """Save objects to file"""
        with open(cls.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objects, f, indent=2)
        cls.__objects = objects

    @classmethod
    def _get_objects(cls):
        """Get all objects (load from file if needed)"""
        if not cls.__objects and os.path.exists(cls.__file_path):
            cls.load_from_file()
        return cls.__objects
