"""The {{ cookiecutter.project_title }} Flask app factory.

This module provides the :func:`create_app` function to create a new
application instance.
"""

import os
import sys

from flask import Flask

from .db import db, migrate
from .main import main as main_blueprint
from .sentry import sentry


def create_app(config=None, **kwargs):
    """Create a new {{ cookiecutter.project_title }} app.

    :param config: the full path to the configuration file.  If none is
                   given, it is assumed that the path is defined in the
                   ``{{ cookiecutter.project_slug|upper }}_CONFIG`` environment variable.
                   If that variable is not set, a warning will be issued
                   if no settings have been provided as keyword
                   arguments either.
    :param kwargs: configuration settings for the Flask application that
                   will take precedence over the settings in the
                   configuration file.  Only keys in uppercase are
                   considered.
    """
    # Create application instance and load basic configuration
    app = Flask(__name__.split(".")[0])
    app.config.from_object("{{ cookiecutter.project_slug }}.config")

    # Parse additional settings from keyword arguments
    kwargs_config = filter_config_values(kwargs)

    # Fall back to configuration file from environment variable
    if config is None:
        config = os.environ.get("{{ cookiecutter.project_slug|upper }}_CONFIG")

    # Load configuration file
    if config:
        try:
            app.config.from_pyfile(config)
        except IOError:
            sys.stderr.write("Cannot read config file: {}\n".format(config))
            sys.exit(2)
        except:  # noqa: E722
            sys.stderr.write("Cannot load config file: {}\n".format(config))
            raise
    elif not kwargs_config:
        sys.stderr.write("No configuration given, using defaults\n")

    # Override config with values from kwargs
    app.config.update(kwargs_config)

    # Initialize extensions
    initialize_extensions(app)

    # Register blueprints and return the application object
    register_blueprints(app)
    return app


def filter_config_values(input_dict):
    """Filter a dictionary for valid configuration values.

    >>> input_dict = {"ONE": 1, "two": 2, "THREE": 3, "FO_FOUR": 4}
    >>> output = filter_config_values(input_dict)
    >>> sorted(output.items())
    [('FO_FOUR', 4), ('ONE', 1), ('THREE', 3)]

    :param input_dict: the dictionary to filter.
    :type input_dict: dict
    :return: a new dictionary with all items from the input dictionary
             that have all-uppercase keys.
    :rtype: dict
    """
    output = {key: input_dict[key] for key in input_dict if key.isupper()}
    return output


def initialize_extensions(app):
    """Initialize extensions on a Flask application instance.

    :param app: a :class:`Flask` application instance
    :type app: Flask
    """
    # Initialize database
    if "SQLALCHEMY_ECHO" not in app.config:
        # Echo SQL queries by default in debug mode
        app.config["SQLALCHEMY_ECHO"] = app.debug
    db.init_app(app)
    migrate.init_app(app)

    # Configure Sentry integration
    if app.config.get("SENTRY_DSN"):
        sentry.init_app(app, dsn=app.config["SENTRY_DSN"])


def register_blueprints(app):
    """Register application blueprints on a Flask application instance.

    :param app: a :class:`Flask` application instance
    :type app: Flask
    """
    url_map = {None: main_blueprint}
    for url_prefix, blueprint in url_map.items():
        app.register_blueprint(blueprint, url_prefix=url_prefix)
