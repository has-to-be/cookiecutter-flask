Flask Cookiecutter
==================

A [Cookiecutter][1] template for [Flask][2] projects.

Python 3.5 is the minimum required Python version to be able to run the Flask
project; for development purposes, however, it is recommended to use
Python 3.6.

[1]: https://cookiecutter.readthedocs.io/en/latest/
[2]: http://flask.pocoo.org/


Prerequisites
-------------

Naturally, you need Cookiecutter on your system first.  Installation is
straightforward via pip:

```console
$ pip3 install --user cookiecutter
```

Additionally, the Flask project provided by this Cookiecutter uses [Poetry][3]
for dependency management.

```console
$ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3
```

This Cookiecutter has been tested with Poetry 0.12.14.  If you happen to have
an older version of Poetry installed on your system, you might want to update
it first to the latest version by running:

```console
$ poetry self:update
```

[3]: https://poetry.eustace.io/


Quickstart
----------

Starting a new Flask project with this Cookiecutter is straightforward:

```console
$ cookiecutter https://github.com/has-to-be/cookiecutter-flask.git
```

You will be prompted for a project name and a project slug, the latter of
which must be a valid Python identifier that does not start with an underscore
character.  You will also be asked for an optional project description as well
as author information.

Once all steps are done, you will end up with a new directory named after the
project slug.  Change into that directory, create and activate a new Python 3
virtualenv (if you haven’t already), and install all dependencies:

```console
$ poetry install
```

That’s it!  Now execute `flask run` or even `<project_slug> run` to launch the
Flask development server, and start developing.
