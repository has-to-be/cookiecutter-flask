"""Tests for the package module."""


def test_exports_application_factory():
    """Verify that the application factory function is exported."""
    from .. import create_app  # noqa: F401
