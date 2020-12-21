"""Tests for the ``app`` module."""

import os

import pytest
import sentry_sdk

from ..app import create_app
from ..config import SECRET_KEY, SESSION_COOKIE_NAME


config_envvar = "{{ cookiecutter.project_slug|upper }}_CONFIG"


def assert_empty_stderr(capsys):
    """Assert that standard error contains nothing."""
    stdout, stderr = capsys.readouterr()
    assert stderr == ""


def test_create_app(capsys):
    """Test app creation without parameters.

    The application should echo a warning and run with default settings.
    """
    app = create_app()
    stdout, stderr = capsys.readouterr()
    assert stderr == "No configuration given, using defaults\n"
    assert app.config["SECRET_KEY"] == SECRET_KEY
    assert app.config["SESSION_COOKIE_NAME"] == SESSION_COOKIE_NAME


def test_create_app_with_conffile(capsys, tmpdir):
    """Test app creation with a config file.

    The application should not echo a warning, and the settings from the
    given config file should override the default settings.
    """
    conffile = tmpdir.join("myconfig.py")
    conf_secret_key = "youcannotguessme"
    conffile.write('SECRET_KEY = "{}"'.format(conf_secret_key))
    app = create_app(str(conffile))
    assert_empty_stderr(capsys)
    assert app.config["SECRET_KEY"] == conf_secret_key
    assert app.config["SESSION_COOKIE_NAME"] == SESSION_COOKIE_NAME


def test_create_app_with_non_existing_conffile(capsys):
    """Test app creation with a non-existing config file.

    Application creation should fail, and an error message should be
    printed.
    """
    conffile = "/this/path/does/not/exist"
    with pytest.raises(SystemExit):
        create_app(conffile)
    stdout, stderr = capsys.readouterr()
    assert stderr == "Cannot read config file: {}\n".format(conffile)


def test_create_app_with_invalid_conffile(capsys, tmpdir):
    """Test app creation with an invalid config file.

    Application creation should fail, and an error message should be
    printed.
    """
    conffile = tmpdir.join("myconfig.py")
    conffile.write('SECRET_KEY = "missingclosingquote')
    with pytest.raises(Exception):
        create_app(str(conffile))
    stdout, stderr = capsys.readouterr()
    assert stderr == "Cannot load config file: {}\n".format(conffile)


def test_create_app_with_environment_variable(capsys, monkeypatch, tmpdir):
    """Test app creation with an environment variable.

    The application should not echo a warning, and the default settings
    should be overriden from the config file that is defined in the
    ``{{ cookiecutter.project_slug|upper }}_CONFIG`` environment variable.
    """
    envfile = tmpdir.join("myconfig.py")
    env_secret_key = "youllneverguessme"
    envfile.write('SECRET_KEY = "{}"'.format(env_secret_key))
    monkeypatch.setitem(os.environ, config_envvar, str(envfile))
    app = create_app()
    assert_empty_stderr(capsys)
    assert app.config["SECRET_KEY"] == env_secret_key
    assert app.config["SESSION_COOKIE_NAME"] == SESSION_COOKIE_NAME


def test_create_app_with_kwargs(capsys):
    """Test app creation with kwargs.

    No warning should be echoed, and the keyword argument settings
    should override the default settings.
    """
    kwargs_secret_key = "donteventryguessingme"
    app = create_app(SECRET_KEY=kwargs_secret_key)
    assert_empty_stderr(capsys)
    assert app.config["SECRET_KEY"] == kwargs_secret_key
    assert app.config["SESSION_COOKIE_NAME"] == SESSION_COOKIE_NAME


def test_create_app_with_conffile_and_envvar(capsys, monkeypatch, tmpdir):
    """Test app creation with config file and environment variable.

    No warning should be echoed, and the settings from the config file
    should override the default settings.  The settings from the file
    provided via the environment variable should be ignored.
    """
    conffile = tmpdir.join("myconfig-conf.py")
    conf_secret_key = "guessingisoverrated"
    conffile.write('SECRET_KEY = "{}"'.format(conf_secret_key))
    envfile = tmpdir.join("myconfig-env.py")
    envfile.write('SECRET_KEY = "guesswhat"')
    monkeypatch.setitem(os.environ, config_envvar, str(envfile))
    app = create_app(str(conffile))
    assert_empty_stderr(capsys)
    assert app.config["SECRET_KEY"] == conf_secret_key
    assert app.config["SESSION_COOKIE_NAME"] == SESSION_COOKIE_NAME


def test_create_app_with_conffile_and_kwargs(capsys, tmpdir):
    """Test app creation with config file and keyword arguments.

    No warning should be echoed, and the settings from the config file
    should override the default settings.  Finally, the settings from
    the keyword arguments should override again.
    """
    conffile = tmpdir.join("myconfig.py")
    conf_cookie_name = "enoznaf"
    conffile.write(
        'SECRET_KEY = "doomedtoguess"\n'
        'SESSION_COOKIE_NAME = "{}"'.format(conf_cookie_name)
    )
    kwargs_secret_key = "makeaneducatedguess"
    app = create_app(str(conffile), SECRET_KEY=kwargs_secret_key)
    assert_empty_stderr(capsys)
    assert app.config["SECRET_KEY"] == kwargs_secret_key
    assert app.config["SESSION_COOKIE_NAME"] == conf_cookie_name


def test_create_app_with_envvar_and_kwargs(capsys, monkeypatch, tmpdir):
    """Test app creation with config file and keyword arguments.

    No warning should be echoed, and the settings from the file provided
    via the environment variable should override the default settings.
    Finally, the settings from the keyword arguments should override
    again.
    """
    envfile = tmpdir.join("myconfig.py")
    env_cookie_name = "enoznaf"
    envfile.write(
        'SECRET_KEY = "reallyhardtoguess"\n'
        'SESSION_COOKIE_NAME = "{}"'.format(env_cookie_name)
    )
    monkeypatch.setitem(os.environ, config_envvar, str(envfile))
    kwargs_secret_key = "guessthis"
    app = create_app(SECRET_KEY=kwargs_secret_key)
    assert_empty_stderr(capsys)
    assert app.config["SECRET_KEY"] == kwargs_secret_key
    assert app.config["SESSION_COOKIE_NAME"] == env_cookie_name


def test_create_app_with_conffile_and_envvar_and_kwargs(
    capsys, monkeypatch, tmpdir
):
    """Test app creation with config file, environment variable, and kwargs.

    No warning should be echoed, and the settings from the config file
    should override the default settings.  Finally, the settings from
    the keyword arguments should override again.  The settings from the
    file provided via the environment variable should be ignored.
    """
    conffile = tmpdir.join("myconfig-conf.py")
    conf_cookie_name = "guesssomuch"
    conffile.write(
        'SECRET_KEY = "guesssomuch"\n'
        'SESSION_COOKIE_NAME = "{}"'.format(conf_cookie_name)
    )
    envfile = tmpdir.join("myconfig-env.py")
    envfile.write(
        'SECRET_KEY = "dontguesssomuch"\nSESSION_COOKIE_NAME = "nevermind"'
    )
    monkeypatch.setitem(os.environ, config_envvar, str(envfile))
    kwargs_secret_key = "youllnevergessitright"
    app = create_app(str(conffile), SECRET_KEY=kwargs_secret_key)
    assert_empty_stderr(capsys)
    assert app.config["SECRET_KEY"] == kwargs_secret_key
    assert app.config["SESSION_COOKIE_NAME"] == conf_cookie_name


def test_create_app_with_sentry_initialization():
    """Test Sentry initialization during app creation."""
    assert sentry_sdk.Hub.current.client is None
    dsn = "http://key@sentry.example.com/4711"
    create_app(SENTRY_DSN=dsn)
    assert sentry_sdk.Hub.current.client.dsn == dsn


def test_create_app_sqlalchemy_echo_default():
    """Test that ``SQLALCHEMY_ECHO`` is not set by default."""
    app = create_app()
    assert app.config["SQLALCHEMY_ECHO"] is False


def test_create_app_sqlalchemy_echo_debug_mode():
    """Test that ``SQLALCHEMY_ECHO`` is not set by default in debug mode."""
    app = create_app(DEBUG=True)
    assert app.config["SQLALCHEMY_ECHO"] is False


def test_create_app_sqlalchemy_echo_explicit_set():
    """Test that ``SQLALCHEMY_ECHO`` is active if explicitly set."""
    app = create_app(SQLALCHEMY_ECHO=True)
    assert app.config["SQLALCHEMY_ECHO"] is True
