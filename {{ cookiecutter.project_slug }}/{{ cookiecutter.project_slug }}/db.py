"""Database integration via SQLAlchemy.

This module instantiates a `Flask-SQLAlchemy`_ instance and a
`Flask-Migrate`_ instance, both of which must later be initialized with
a Flask application instance:

.. code-block:: python

   db.init_app(app)
   migrate.init_app(app)

.. _Flask-SQLAlchemy: http://flask-sqlalchemy.pocoo.org/
.. _Flask-Migrate: https://flask-migrate.readthedocs.io/
"""

import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


migrations_dir = os.path.join(os.path.dirname(__file__), "migrations")

db = SQLAlchemy()
migrate = Migrate(db=db, directory=migrations_dir)
