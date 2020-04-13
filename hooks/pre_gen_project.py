import keyword
import sys


errors = []


# Validate the Project’s title, which must be at most 50 characters long.

project_title = "{{ cookiecutter.project_title|replace('"', '\\"') }}"

if len(project_title) < 1:
    errors.append("Project title is too short.")

if len(project_title) > 50:
    errors.append("Project title is longer than 50 characters.")


# Validate the Project’s slug, which must be a valid lowercased Python
# identifier (but not a keyword!) with at most 20 characters that does not
# start with an underscore character.

project_slug = "{{ cookiecutter.project_slug }}"

if len(project_slug) < 2:
    errors.append("Project slug is too short.")

if len(project_slug) > 20:
    errors.append("Project slug is longer than 20 characters.")

if not project_slug.isidentifier():
    errors.append("Project slug is not a valid Python identifier.")

if keyword.iskeyword(project_slug):
    errors.append("Project slug is a reserved Python keyword.")

if project_slug.startswith("_"):
    errors.append("Project slug starts with an underscore.")

if not project_slug.islower():
    errors.append("Project slug is not all-lowercase.")


# If there were any errors, print them and abort.

if errors:
    error_lines = "\n".join("  * {}".format(error) for error in errors)
    message = "\nERRORS:\n\n{}\n".format(error_lines)
    sys.exit(message)
