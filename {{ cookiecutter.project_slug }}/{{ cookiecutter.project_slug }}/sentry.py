"""{{ cookiecutter.project_title }} Sentry integration.

This module instantiates a Sentry client, which must later be
initialized with a Flask application instance:

.. code-block:: python

   sentry.init_app(app, dsn="https://*****@<host>/<project>")

The client will not only send uncaught exceptions to Sentry, but also
logging messages with level ``ERROR``.
"""

import logging

from raven.contrib.flask import Sentry


sentry = Sentry(logging=True, level=logging.ERROR)
