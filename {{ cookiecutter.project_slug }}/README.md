{{ cookiecutter.project_title }}
{{ "=" * cookiecutter.project_title|length }}

Quickstart
----------

 1. Make sure you have [Poetry][1] installed on you local system.

        $ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python3

 2. Create and activate a Python 3.5 (or higher) virtualenv if you haven't
    done so yet.  Use your preferred virtualenv management tool, or leverage
    Python's built-in capabilities:

        $ python3 -m venv venv
        $ source venv/bin/activate

 3. Install the project dependencies:

        $ poetry install

 4. Launch the dockerized service dependencies, prepare the database, and fire
    up the built-in development web server:

        $ docker-compose up -d
        $ {{ cookiecutter.project_slug }} db upgrade
        $ {{ cookiecutter.project_slug }} run

 5. Run the test suite:

        $ pytest

[1]: https://poetry.eustace.io/


Development Notes
-----------------

### Git

You can install a Git pre-commit hook that will automatically check the code
style every time you run `git commit`:

    $ pre-commit install

Once installed, `git commit` will abort if any check fails.


### PyCharm/IntelliJ IDEA Integration

If you want to run the test suite inside PyCharm or IntelliJ with enabled
debugger, you must add `--no-cov` as *Additional Argument* to the *Run/Debug
Configuration* (see [this answer on StackOverflow][2]).

[2]: https://stackoverflow.com/questions/40718760/unable-to-debug-in-pycharm-with-pytest
