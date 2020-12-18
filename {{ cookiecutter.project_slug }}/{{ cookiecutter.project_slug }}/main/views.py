"""Views for the ``main`` blueprint."""

from flask import current_app, Response

from .blueprint import main


@main.route("/")
def index():
    """Show a plain text welcome message."""
    message = "This is {{ cookiecutter.project_title|replace('"', '\\"') }}!\n"
    response = Response(message, mimetype="text/plain")
    return response


@main.route("/.well-known/healthcheck")
def healthcheck():
    """Return status information (as JSON), usable for health checks."""
    version = current_app.config["SENTRY_RELEASE"]
    return {"status": "OK", "version": version}
