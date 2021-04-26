APP_NAME := associations

install:
	poetry install

up:
	docker-compose up --force-recreate --build

stop:
	docker-compose stop

test: black flake8 pylint mypy pytest

black:
	poetry run black $(APP_NAME) tests
flake8:
	poetry run flake8
mypy:
	poetry run mypy $(APP_NAME)
pylint:
	poetry run pylint $(APP_NAME) --fail-under=8
pytest:
	poetry run pytest tests --log-cli-level=INFO

