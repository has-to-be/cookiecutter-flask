"""The {{ cookiecutter.project_title }} web application.

The package itself only exports the :func:`create_app` factory function
to create a new Flask application instance.
"""

from .app import create_app  # noqa: F401
