# agileHelper

## Description

The agileHelper is a tool for Scrum Masters, Facilitators or any other agile role who want to have a much better way of
handling their teams.

## Key features are:

- team management
- create a tool box which is available for the whole user group
- manage todos via a simple kanban board
- plan and execute meetings, like Dailies or Retrospectives

---

# Development

## Project settings and structure

- Each app has its own template folder.
- Only common templates are located within the global templates folder.
- This project is optimized to run on DigitalOcean.


## Database

In debug mode, the local SQLite3 database is in use. If necessary, switch to PostgreSQL (via Docker).

## Superuser

- A superuser has to be created manually.

## Windows

- venv\Scripts\Activate.ps1
- pip install -r requirements.txt
- New-Item -Path Env:\READ_DOT_ENV_FILE -Value True
- python manage.py collectstatic --no-input
- python .\manage.py migrate
- python .\manage.py runserver

## Mac

- source venv\bin\activate
- pip install -r requirements.txt
- export READ_DOT_ENV_FILE=True
- python manage.py collectstatic --no-input
- python .\manage.py migrate
- python .\manage.py runserver

## DigitalOcean

python manage.py collectstatic --no-input && python manage.py migrate && gunicorn --worker-tmp-dir /dev/shm agilehelper.wsgi