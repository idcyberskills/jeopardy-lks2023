#!/usr/bin/env sh

# Web application initialization
python3 manage.py collectstatic --clear --noinput
python3 manage.py migrate
python3 manage.py loaddata fixtures/init.json
/entrypoint.sh