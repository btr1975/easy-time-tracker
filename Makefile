# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 2.0.2
#

.PHONY: all info build build-container coverage format pylint pytest gh-pages build \
	check-vuln check-security pip-export mypy complexipy

info:
	@echo "make options"
	@echo "    all                 To run coverage, format, pylint, and check-vuln"
	@echo "    build               To build a distribution"
	@echo "    check-vuln          To check for vulnerabilities in the dependencies"
	@echo "    check-security      To check for vulnerabilities in the code"
	@echo "    coverage            To run coverage and display ASCII and output to htmlcov"
	@echo "    format              To format the code with black"
	@echo "    mypy                To run mypy"
	@echo "    pylint              To run pylint"
	@echo "    pytest              To run pytest with verbose option"
	@echo "    pip-export          To export the requirements to requirements.txt and requirements-dev.txt"
	@echo "    gh-pages           To create the GitHub pages"



all: format complexipy pylint mypy coverage check-security pip-export

build:
	@uv build --wheel --sdist

coverage:
	@uv run pytest --cov --cov-report=html -vvv

format:
	@uv run black easy_time_tracker/
	@uv run black tests/

pylint:
	@uv run pylint easy_time_tracker/

pytest:
	@uv run pytest --cov -vvv

check-security:
	@uv run bandit -c pyproject.toml -r .

mypy:
	@uv run mypy easy_time_tracker/

pip-export:
	@uv export --no-dev --no-emit-project --no-editable > requirements.txt
	@uv export --no-emit-project --no-editable > requirements-dev.txt

gh-pages:
	@rm -rf ./docs/source/code
	@uv run sphinx-apidoc -o ./docs/source/code ./easy_time_tracker
	@uv run sphinx-build ./docs ./docs/gh-pages

complexipy:
	@uv run complexipy
