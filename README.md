Flask Cookiecutter
==================

A [Cookiecutter][1] template for [Flask][2] projects.

[1]: https://cookiecutter.readthedocs.io/en/latest/
[2]: https://flask.palletsprojects.com/


Prerequisites
-------------

Naturally, you need Cookiecutter on your system first.  Installation is
straightforward via pip:

```console
$ pip3 install --user cookiecutter
```

Additionally, you will need [Docker][3] in order to run the Flask project.

[3]: https://www.docker.com/


Quickstart
----------

Starting a new Flask project with this Cookiecutter is dead simple:

```console
$ cookiecutter https://github.com/has-to-be/cookiecutter-flask.git
```

You will be prompted for a project name and a project slug, the latter of
which must be a valid Python identifier that does not start with an underscore
character.  You will also be asked for an optional project description as well
as author information.

Once all steps are done, you will end up with a new directory named after the
project slug.  Change into that directory and launch the service with the
built-in Flask development server:

```console
$ docker-compose up -d
```

That’s it!
