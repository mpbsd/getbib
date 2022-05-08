OPR_SYSTEM = $(shell uname -s)

build:
	python -m pkgs.main

.PHONY: build black clean ready

black:
	black -l 80 pkgs/main.py

clean:
	find . -type d -name __pycache__ | xargs rm -rf

ready:
	python -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	deactivate
