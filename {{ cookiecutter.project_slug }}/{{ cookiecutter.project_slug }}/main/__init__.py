"""The ``main`` Flask blueprint.

The package itself exports the blueprint object as :data:`main`, so you
can register it on your Flask application instance with:

.. code-block:: python

   from {{ cookiecutter.project_slug }}.main import main
   app.register_blueprint(main)
"""

from .blueprint import main  # noqa: F401
