install:
	poetry install

start:
	poetry run python manage.py runserver
	# poetry run python manage.py runserver 0.0.0.0:8000
