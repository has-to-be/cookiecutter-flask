FROM python:3.5

# Create application directory, and copy local sources into it
RUN mkdir /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

# Install Python dependencies (through Poetry)
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install

# Expose the development web server’s port
EXPOSE 5000

# By default, run the Flask development web server
CMD flask run --host 0.0.0.0
