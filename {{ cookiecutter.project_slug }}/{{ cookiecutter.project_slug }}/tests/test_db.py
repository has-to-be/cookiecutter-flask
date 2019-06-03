"""Tests for the ``db`` module."""

import re

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from ..db import db, migrate, ReprMixin


def test_db_is_flask_sqlalchemy_instance():
    """Verify that :data:`db` is a :class:`SQLAlchemy` instance."""
    assert isinstance(db, SQLAlchemy)


def test_migrate_is_flask_migrate_instance():
    """Verify that :data:`migrate` is a :class:`Migrate` instance."""
    assert isinstance(migrate, Migrate)


class MyReprModel(ReprMixin):
    """Dummy class for testing the :class:`ReprMixin`."""


class TestReprMixin:
    """Tests for the :class:`ReprMixin` class."""

    def test_object_with_id(self):
        """Check the representation string of an object with an ID."""
        my_object = MyReprModel()
        my_object.id = 49
        assert repr(my_object) == "<MyReprModel #49>"

    def test_object_without_id(self):
        """Check the representation string of an object without an ID."""
        my_object = MyReprModel()
        assert re.match(r"^<MyReprModel 0x[0-9a-f]+>", repr(my_object))

    def test_object_with_none_id(self):
        """Check the representation string of an object with a ``None`` ID."""
        my_object = MyReprModel()
        my_object.id = None
        assert re.match(r"^<MyReprModel 0x[0-9a-f]+>", repr(my_object))

    def test_object_with_empty_id(self):
        """Check the representation string of an object with an empty ID."""
        my_object = MyReprModel()
        my_object.id = ""
        assert re.match(r"^<MyReprModel 0x[0-9a-f]+>", repr(my_object))
