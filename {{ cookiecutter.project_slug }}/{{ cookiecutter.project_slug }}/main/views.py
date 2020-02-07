"""Views for the ``main`` blueprint."""

from flask import Response

from .blueprint import main


@main.route("/")
def index():
    """Show a plain text welcome message."""
    message = "This is {{ cookiecutter.project_title }}!\n"
    response = Response(message, mimetype="text/plain")
    return response


@main.route("/.well-known/healthcheck")
def healthcheck():
    """Return status information (as JSON), usable for health checks."""
    return {"status": "OK"}
