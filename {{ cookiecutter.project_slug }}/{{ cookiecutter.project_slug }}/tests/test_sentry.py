"""Tests for the ``sentry`` module."""

from raven.contrib.flask import Sentry

from ..sentry import sentry


def test_sentry_object_is_sentry_instance():
    """Verify that :data:`sentry` is a :class:`Sentry` instance."""
    assert isinstance(sentry, Sentry)
