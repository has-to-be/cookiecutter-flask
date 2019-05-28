message = """\
-------------------------------------------------------------------------------

Congratulations, you did it!  Now:

 1. Change into your project directory, and create and activate a Python 3.5
    (or higher) virtualenv if you haven't done so yet.  Use your preferred
    virtualenv management tool, or leverage Python's built-in capabilities:

        $ cd {{ cookiecutter.project_slug }}
        $ python3 -m venv venv
        $ source venv/bin/activate

 2. Install the project dependencies:

        $ poetry install

 3. Launch the dockerized service dependencies and fire up the built-in
    development web server:

        $ docker-compose up -d
        $ {{ cookiecutter.project_slug }} run

 4. Run the test suite:

        $ pytest
"""
print(message)
