"""Set up and configure the ``main`` blueprint."""

from flask import Blueprint


main = Blueprint("main", __name__, cli_group=None)

from . import cli, views  # noqa: F401, I100, I202
