"""A simple visit to the {{ cookiecutter.project_title }}."""

from .base import FunctionalTest


class HomePageTest(FunctionalTest):
    """Tests for the home page."""

    def test_project_title_in_home_page_source(self):
        """Verify that the home page source contains the project title."""
        self.browser.get(self.get_server_url())
        project_title = "{{ cookiecutter.project_title }}"
        assert project_title in self.browser.page_source
