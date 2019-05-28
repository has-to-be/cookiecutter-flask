"""Tests for the ``wsgi`` module."""

from flask import Flask

from ..wsgi import application


def test_application_is_flask_instance():
    """Verify that :data:`application` is a :class:`Flask` instance."""
    assert isinstance(application, Flask)
