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


# Flask settings
# --------------
SECRET_KEY = os.environ.get("{{ cookiecutter.project_slug|upper }}_APP_SECRET", "changeme")
SESSION_COOKIE_NAME = "{{ cookiecutter.project_slug }}"


# Flask-SQLAlchemy settings
# -------------------------
SQLALCHEMY_DATABASE_URI = "postgresql://postgres@postgres/postgres"


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
SQLALCHEMY_TRACK_MODIFICATIONS = False
