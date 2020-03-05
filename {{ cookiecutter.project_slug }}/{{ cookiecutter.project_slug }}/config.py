"""{{ cookiecutter.project_title }} default settings."""

import os

# Customizable configuration
# ==========================
#
# Consider all settings in this section to be “public”, i.e., consider
# potentially any of them to be configured differently in concrete
# application instances.


# Application settings
# --------------------
#
# Put your own application-specific settings here.

# Configure logging
{{ cookiecutter.project_slug|upper }}_LOGGING = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
        # # for production, contemplate using JSONified log messages
        # "json": {
        #     "class": "{{ cookiecutter.project_slug }}.logging.CustomJsonFormatter",
        #     "format": (
        #         "(datetime) (level) (logger) (message) "
        #         "(source) (lineno) (function)"
        #     ),
        # },
    },
    "handlers": {
        "stream": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "{{ cookiecutter.project_slug }}": {
            "level": "DEBUG",
            "propagate": False,
            "handlers": ["stream"],
        },
        # # Enable SQL statement logging
        # "sqlalchemy.engine": {"level": "INFO"},
    },
    "root": {"level": "INFO", "handlers": ["stream"]},
}

# Flask settings
# --------------
SECRET_KEY = os.environ.get("{{ cookiecutter.project_slug|upper }}_APP_SECRET", "changeme")
SESSION_COOKIE_NAME = "{{ cookiecutter.project_slug }}"


# Flask-SQLAlchemy settings
# -------------------------
SQLALCHEMY_DATABASE_URI = "postgresql://postgres@localhost/postgres"


# Sentry settings
# ---------------
# SENTRY_DSN = "<protocol>://<key>@<host>/<project>"
SENTRY_ENVIRONMENT = "development"


# Application-internal configuration
# ==================================
#
# Consider all settings in this section to be “private”, i.e., they
# should never be changed.


# Flask-SQLAlchemy settings
# -------------------------
# Set the ``sqlalchemy.engine`` logger’s log level to ``INFO`` or
# ``DEBUG`` if you want to see the executed SQL statements.
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
