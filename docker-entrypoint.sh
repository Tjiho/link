#!/bin/sh
cd /code/link

/venv/bin/python manage.py collectstatic --noinput
/venv/bin/python manage.py makemigrations webApp
/venv/bin/python manage.py migrate
/bin/chmod 666 db.sqlite

exec "$@"
