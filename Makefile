install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

run-dev:
	python run.py

test:
	pytest tests/ -v --cov=app
