{{ cookiecutter.project_title }}
{{ "=" * cookiecutter.project_title|length }}

Quickstart
----------

 1. Install and launch the dockerized service with its dependencies:

        $ ./do up -d

 2. Prepare the database:

        $ ./do flask db upgrade

 3. Verify that the service is up and running by requesting its health check
    endpoint:

        $ curl http://localhost:5000/.well-known/healthcheck

 4. Run the test suite:

        $ ./do test


Development Notes
-----------------

### Poetry

To install or update dependencies, you must execute `poetry` inside a running
service container.  From the repository root, run:

    $ ./do poetry [...]

Afterwards, stop the services, and use the `--build` flag to rebuild the
Docker image with the new dependencies when starting the service again:

    $ ./do stop
    $ ./do up -d --build


### Git

You can install a Git pre-commit hook that will automatically check the code
style every time you run `git commit`.  Make sure that you have set up the
[pre-commit][1] helper program on your local machine, and execute:

    $ pre-commit install

Once installed, `git commit` will abort if any check fails.

[1]: https://pre-commit.com/


### PyCharm/IntelliJ IDEA Integration

If you want to run the test suite inside PyCharm or IntelliJ with enabled
debugger, you must add `--no-cov` as *Additional Argument* to the *Run/Debug
Configuration* (see [this answer on StackOverflow][2]).

[2]: https://stackoverflow.com/questions/40718760/unable-to-debug-in-pycharm-with-pytest


### Working with Other Dockerized Services

#### Connecting

In a microservices-oriented environment, chances are that you will want to
connect this web application to another dockerized service.  To achieve this,
you need to add the other service’s Docker network to this service’s
*docker-compose.yml*.

For example, if the network of the service you want to connect to was named
*smartservice_api*, you could set it up like this:

```yaml
services:
  web:
    build: .
    [...]
    networks:
      - default
      - api
      - smartservice  # a docker-compose internal name

networks:
  default:
  api:
  smartservice:  # the same docker-compose internal name as above
    external:
      name: smartservice_api
```


#### Shared Services

If you need to connect two dockerized applications, make sure to not start a
shared service twice, e.g., RabbitMQ.  In this service’s *docker-compose.yml*,
only declare services that are used exclusively by this web application in the
*web* container’s `depends_on` section.  Then, launch the full Docker Compose
application that contains the shared service, and only the *web* container of
this application:

    $ ./do up web -d
