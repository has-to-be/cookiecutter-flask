"""The {{ cookiecutter.project_title }} CLI.

You can use this module’s :func:`main` function as console script entry
point in your ``setup.py``, for example:

.. code-block:: python

   from setuptools import setup

   setup(
       ...,
       entry_points={
           'console_scripts': [
               '{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.cli:main'
           ]
       }
   )

This allows you to run commands simply via:

.. code-block:: console
   $ {{ cookiecutter.project_slug }} ...
"""

import click
from flask.cli import FlaskGroup

from .app import create_app


def _create_app_instance(script_info):
    """Create an application instance."""
    return create_app()


@click.group(cls=FlaskGroup, create_app=_create_app_instance)
def main():
    """Run Flask-CLI."""
