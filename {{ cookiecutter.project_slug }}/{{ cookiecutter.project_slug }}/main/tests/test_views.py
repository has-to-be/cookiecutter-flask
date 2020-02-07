"""Tests for the ``main`` blueprint’s views."""

from http import HTTPStatus

from ...tests.base import TestCaseBase


class TestIndexView(TestCaseBase):
    """Tests for the index view."""

    def test_index_welcome_message(self):
        """Check that the index view returns a plain text welcome message."""
        response = self.client.get("/")
        message = response.get_data().decode()
        assert response.mimetype == "text/plain"
        assert "{{ cookiecutter.project_title }}" in message


class TestHealthcheck(TestCaseBase):
    """Tests for the healthcheck view."""

    def get_default_response(self):
        """Call the view without parameters, and return the response.

        :rtype: flask.Flask.response_class
        """
        response = self.client.get("/.well-known/healthcheck")
        return response

    def test_json_content_type(self):
        """Verify that the response uses the JSON content type."""
        response = self.get_default_response()
        assert response.mimetype == "application/json"

    def test_http_status_code_ok(self):
        """Check that the response is served with HTTP status “OK”."""
        response = self.get_default_response()
        assert response.status_code == HTTPStatus.OK

    def test_response_contains_status(self):
        """Verify that the response contains status information."""
        response = self.get_default_response()
        data = response.get_json()
        assert data["status"] == "OK"
