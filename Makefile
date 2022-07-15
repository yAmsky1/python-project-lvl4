install:
	poetry install

run-server:
	poetry run python manage.py runserver

requirements:
	poetry export --without-hashes -f requirements.txt --output requirements.txt

lint:
	poetry run flake8 task_manager
