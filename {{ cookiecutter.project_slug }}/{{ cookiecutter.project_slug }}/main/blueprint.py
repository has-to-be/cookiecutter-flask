"""Set up and configure the ``main`` blueprint."""

from flask import Blueprint


main = Blueprint("main", __name__)

from . import views  # noqa: F401, I100, I202
