"""Tests for the ``main`` blueprint’s views."""

from ...tests.base import TestCaseBase


class TestIndexView(TestCaseBase):
    """Tests for the index view."""

    def test_index_welcome_message(self):
        """Check that the index view returns a plain text welcome message."""
        response = self.client.get("/")
        message = response.get_data().decode()
        assert response.mimetype == "text/plain"
        assert "{{ cookiecutter.project_title }}" in message
