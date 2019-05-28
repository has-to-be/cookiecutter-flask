"""Common classes and utilities for functional tests."""

import multiprocessing
import os
import socketserver
import time

import coverage
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from {{ cookiecutter.project_slug }}.tests.base import clean_db, create_test_app, init_db


live_host = os.environ.get("{{ cookiecutter.project_slug|upper }}_LIVETEST_HOST", "127.0.0.1")


class FunctionalTest(LiveServerTestCase):
    """Base class for functional tests."""

    def create_app(self):
        """Create the test server application instance."""
        coverage.process_startup()
        app = create_test_app(LIVESERVER_PORT=0)
        selenium_server_url = "http://{}:{}/wd/hub".format(
            os.environ.get("{{ cookiecutter.project_slug|upper }}_SELENIUM_HOST", "127.0.0.1"),
            os.environ.get("{{ cookiecutter.project_slug|upper }}_SELENIUM_PORT", "4444"),
        )
        self.browser = webdriver.Remote(
            selenium_server_url, DesiredCapabilities.CHROME
        )
        self.browser.implicitly_wait(3)
        return app

    def setUp(self):
        """Initialize the database."""
        init_db()

    def tearDown(self):
        """Close the browser, and clean up the database."""
        self.browser.quit()
        clean_db()

    def get_server_url(self):
        """Return the test server’s URL."""
        return "http://{}:{}".format(live_host, self._port_value.value)

    # Override `_spawn_live_server` from the base class in order to be
    # able to set the `host` keyword argument for `app.run()`.  This is
    # needed to potentially make the live server accessible externally,
    # which in turn is necessary for GitLab CI.
    def _spawn_live_server(self):
        self._process = None
        port_value = self._port_value

        def worker(app, port):
            # Based on solution: http://stackoverflow.com/a/27598916
            # Monkey-patch the server_bind so we can determine the port
            # bound by Flask.  This handles the case where the port
            # specified is `0`, which means that the OS chooses the
            # port.  This is the only known way (currently) of getting
            # the port out of Flask once we call `run`.
            original_socket_bind = socketserver.TCPServer.server_bind

            def socket_bind_wrapper(self):
                ret = original_socket_bind(self)
                # Get the port and save it into the port_value, so the
                # parent process can read it.
                (_, port) = self.socket.getsockname()
                port_value.value = port
                socketserver.TCPServer.server_bind = original_socket_bind
                return ret

            socketserver.TCPServer.server_bind = socket_bind_wrapper
            app.run(host=live_host, port=port, use_reloader=False)

        self._process = multiprocessing.Process(
            target=worker, args=(self.app, self._configured_port)
        )

        self._process.start()

        # We must wait for the server to start listening, but give up
        # after a specified maximum timeout
        timeout = self.app.config.get("LIVESERVER_TIMEOUT", 5)
        start_time = time.time()

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                raise RuntimeError(
                    "Failed to start the server after %d seconds. " % timeout
                )

            if self._can_ping_server():
                break
