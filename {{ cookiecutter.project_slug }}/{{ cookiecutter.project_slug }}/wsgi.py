"""The {{ cookiecutter.project_title }} as a WSGI app."""

from .app import create_app


application = create_app()
