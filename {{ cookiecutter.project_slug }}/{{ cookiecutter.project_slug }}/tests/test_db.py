"""Tests for the ``db`` module."""

import re

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from ..db import db, migrate


def test_db_is_flask_sqlalchemy_instance():
    """Verify that :data:`db` is a :class:`SQLAlchemy` instance."""
    assert isinstance(db, SQLAlchemy)


def test_migrate_is_flask_migrate_instance():
    """Verify that :data:`migrate` is a :class:`Migrate` instance."""
    assert isinstance(migrate, Migrate)
