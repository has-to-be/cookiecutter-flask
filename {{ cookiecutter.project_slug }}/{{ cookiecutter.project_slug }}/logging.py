"""Custom logging functionality."""

import datetime
import sys

from pythonjsonlogger.jsonlogger import JsonFormatter


class CustomJsonFormatter(JsonFormatter):
    """A custom JSON log formatter."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.

        This merely acts as a wrapper to :meth:`JsonFormatter.__init__`,
        setting the ``validate`` keyword argument (supported since
        Python 3.8) to *False* if it was not provided.
        """
        if sys.version_info >= (3, 8, 0):
            kwargs.setdefault("validate", False)
        super().__init__(*args, **kwargs)

    def add_fields(self, log_record, record, message_dict):
        """Add custom fields to a log record.

        This adds a ``datetime`` field which holds the log record’s
        timestamp as UTC in ISO 8601 format with microseconds, e.g.,
        ``2016-03-16T08:02:49.960074Z``.  Additionally, the function
        adds aliases for some field names:

        - ``level`` as an alias for ``levelname``
        - ``logger`` as an alias for ``name``
        - ``source`` as an alias for ``pathname``
        - ``function`` as an alias for ``funcName``

        .. note::
           All added fields are included in *every* log message, even if
           the format does not require them.
        """
        super().add_fields(log_record, record, message_dict)

        # Add a ``datetime`` field with the log entry’s UTC timestamp,
        # including microseconds, and delete the ``timestamp`` field
        # (if it exists).
        if log_record.get("timestamp"):
            timestamp = log_record["timestamp"]
            del log_record["timestamp"]
        else:
            timestamp = datetime.datetime.fromtimestamp(
                record.created, tz=datetime.timezone.utc
            )
        log_record["datetime"] = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        # Add aliases for a few field names
        def add_alias(alias, field):
            if alias in self._required_fields and not log_record.get(alias):
                log_record[alias] = getattr(record, field)

        add_alias("level", "levelname")
        add_alias("logger", "name")
        add_alias("source", "pathname")
        add_alias("function", "funcName")
