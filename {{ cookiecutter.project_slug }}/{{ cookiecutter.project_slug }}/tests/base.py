"""Custom testing utilities and test base classes."""

import os

from flask_migrate import downgrade, upgrade
from flask_testing import TestCase

from ..app import create_app
from ..db import db


def create_test_app(**config):
    """Create an application instance for testing.

    The application is initialized with the ``TESTING`` flag set to
    ``True`` and using the Docker test database.
    """
    test_db = os.environ.get(
        "{{ cookiecutter.project_slug|upper }}_TEST_DB", "postgresql://test@postgres/test"
    )
    test_config = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": test_db}
    test_config.update(**config)
    app = create_app(**test_config)
    return app


def init_db():
    """Initialize the database."""
    upgrade()


def clean_db():
    """Delete database tables."""
    downgrade(revision="base")


class TestCaseBase(TestCase):
    """Base class for unit tests."""

    def create_app(self, **config):
        """Create an application instance and a shortcut to a CLI runner."""
        app = create_test_app(**config)
        self.cli_runner = app.test_cli_runner()
        return app

    def setUp(self):
        """Initialize the database."""
        init_db()

    def tearDown(self):
        """Properly remove SQLAlchemy session, and clean up the database."""
        db.session.remove()
        clean_db()
