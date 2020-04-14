"""CLI commands for the ``main`` blueprint."""

import click

from .blueprint import main


@main.cli.command()
@click.argument("name", default="World")
def welcome(name):
    """Print a “Welcome” message."""
    message = "Welcome to {{ cookiecutter.project_title|replace('"', '\\"') }}, {}!".format(name)
    click.echo(message)
