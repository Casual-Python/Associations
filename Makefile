APP_NAME := associations

install:
	poetry install

test: black flake8 pylint mypy pytest

black:
	poetry run black $(APP_NAME)
flake8:
	poetry run flake8
mypy:
	poetry run mypy $(APP_NAME)
pylint:
	poetry run pylint $(APP_NAME) --fail-under=10
pytest:
	poetry run pytest tests --log-cli-level=INFO

