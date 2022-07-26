install:
	poetry install

run-server:
	poetry run python manage.py runserver

requirements:
	poetry export --without-hashes -f requirements.txt --output requirements.txt

lint:
	poetry run flake8 task_manager

test:
	poetry run python3 manage.py test

messages:
	django-admin makemessages --ignore="static" --ignore=".env" -l ru

compile:
	poetry run django-admin compilemessages --ignore=env

migrations:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate