APP_NAME := associations

install:
	poetry install
black:
	poetry run black $(APP_NAME)
flake8:
	poetry run flake8
pylint:
	poetry run pylint $(APP_NAME) --fail-under=10
pytest:
	poetry run pytest tests --log-cli-level=INFO
test: black flake8 pylint pytest