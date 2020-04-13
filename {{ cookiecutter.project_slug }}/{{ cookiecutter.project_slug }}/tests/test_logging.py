"""Tests for the ``logging`` module."""

import datetime
import json
import logging

import pytest

from ..logging import CustomJsonFormatter


class TestCustomJsonFormatter:
    """Tests for the :class:`CustomJsonFormatter` class."""

    def test_json_output(self, caplog):
        """Verify that the formatter outputs valid JSON."""
        json_formatter = CustomJsonFormatter()
        caplog.handler.setFormatter(json_formatter)
        caplog.set_level(logging.INFO)
        logging.getLogger().info("This is a test")
        # ``json.loads()`` throws a ``ValueError`` if the value is not JSON
        json.loads(caplog.text)

    def test_message_in_message_field(self, caplog):
        """Verify that the log message ends up in the ``message`` field."""
        message = "This is a test"
        json_formatter = CustomJsonFormatter()
        caplog.handler.setFormatter(json_formatter)
        caplog.set_level(logging.INFO)
        logging.getLogger().info(message)
        data = json.loads(caplog.text)
        assert data["message"] == message

    def test_has_datetime_field(self, caplog):
        """Verify that log messages contain a ``datetime`` field."""
        json_formatter = CustomJsonFormatter()
        caplog.handler.setFormatter(json_formatter)
        caplog.set_level(logging.INFO)
        logging.getLogger().info("This is a test")
        data = json.loads(caplog.text)
        datetime.datetime.strptime(data["datetime"], "%Y-%m-%dT%H:%M:%S.%fZ")

    @pytest.mark.parametrize(
        "field, alias",
        [
            ("levelname", "level"),
            ("name", "logger"),
            ("pathname", "source"),
            ("funcName", "function"),
        ],
    )
    def test_alias_definitions(self, caplog, field, alias):
        """Verify that the formatter offers several extra fields."""
        json_formatter = CustomJsonFormatter("({}) ({})".format(field, alias))
        caplog.handler.setFormatter(json_formatter)
        caplog.set_level(logging.INFO)
        logging.getLogger().info("This is a test")
        data = json.loads(caplog.text)
        assert data[field] == data[alias]
