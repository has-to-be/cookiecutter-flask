"""Tests for the ``cli`` module."""

from click import Command, Context
from flask import Flask
from flask.cli import FlaskGroup, ScriptInfo

from ..cli import _create_app_instance, main


def test_main_is_flask_group():
    u"""Check that the :func:`main` function is a :class:`FlaskGroup`."""
    assert isinstance(main, FlaskGroup)


def test_create_app_instance_creates_flask_instance():
    u"""Check that :func:`_create_app_instance` creates a Flask instance."""
    with Context(Command("")):
        application = _create_app_instance(ScriptInfo())
        assert isinstance(application, Flask)
