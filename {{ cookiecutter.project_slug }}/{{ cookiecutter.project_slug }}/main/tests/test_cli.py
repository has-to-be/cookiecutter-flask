"""Tests for the ``main`` blueprint’s CLI commands."""

from ..cli import welcome
from ...tests.base import TestCaseBase


class TestWelcomeCommand(TestCaseBase):
    """Tests for the “welcome” command."""

    def test_message_contains_project_title(self):
        """Check that the project title is part of the welcome message."""
        result = self.cli_runner.invoke(welcome)
        assert "{{ cookiecutter.project_title|replace('"', '\\"') }}" in result.output

    def test_message_greets_world_by_default(self):
        """Check that the whole World is greeted by default."""
        result = self.cli_runner.invoke(welcome)
        assert result.output.endswith("World!\n")

    def test_message_greets_provided_name_by_default(self):
        """Check that the provided “name” argument is greeted."""
        name = "Monty"
        result = self.cli_runner.invoke(welcome, [name])
        assert result.output.endswith("{}!\n".format(name))
