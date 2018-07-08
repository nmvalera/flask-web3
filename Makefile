# A sample Makefile for facilitating development on Flask-Web3.

# Python version
INTERPRETER=python3.6

# Python executable path
VENV=venv
VENV_BIN=$(VENV)/bin
export EXEC_PATH=$(VENV_BIN)/

# Python executables
PYTHON=$(EXEC_PATH)python
PIP=$(EXEC_PATH)pip
COVERAGE=$(EXEC_PATH)coverage
FLAKE8=$(EXEC_PATH)flake8
AUTOFLAKE=$(EXEC_PATH)autoflake
AUTOPEP8=$(EXEC_PATH)autopep8
PYTEST=$(EXEC_PATH)pytest
TOX=$(EXEC_PATH)tox

# General commands
.PHONY: all venv pip-install init develop

# Docs commands
.PHONY: build-docs docs

# Clean commands
.PHONY: clean-docs clean-pyc clean-build clean-tox clean hard-clean

# Linting commands
.PHONY: flake8 autoflake autopep8 auto-lint lint

# Test commands
.PHONY: test-lint test run-coverage coverage tox

venv:
	@echo "Creating venv"
	@virtualenv $(VENV) -p $(INTERPRETER)

install-dev:
	@$(PIP) install -q -e .[dev]

develop: clean-pyc install-dev

init: venv develop

build-docs:
	@$(MAKE) -sC docs build-html

docs:
	@$(MAKE) -sC docs html

clean-docs:
	@$(MAKE) -sC docs clean
	@rm --force --recursive htmlcov/

clean-pyc:
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '__pycache__' -type d | xargs rm -rf

clean-build:
	@rm --force --recursive build/
	@rm --force --recursive dist/
	@rm --force --recursive *.egg-info

clean-tox:
	@rm --force --recursive .tox/

clean: clean-pyc clean-build clean-docs

hard-clean: clean-pyc clean-build clean-docs clean-tox
	@rm --force --recursive .cache/
	@rm --force --recursive venv/
	@rm --force .coverage
	@find . -name '.coverage.*' -exec rm -f {} +

flake8:
	@$(FLAKE8)

test-lint: develop flake8

autoflake:
	@$(AUTOFLAKE) -ir --remove-all-unused-imports --remove-unused-variables ./flask_web3
	@$(AUTOFLAKE) -ir --remove-all-unused-imports --remove-unused-variables ./tests

autopep8:
	@$(AUTOPEP8) -ir --aggressive --max-line-length=120  ./flask_web3
	@$(AUTOPEP8) -ir --aggressive --max-line-length=120  ./tests

auto-lint: autoflake autopep8

lint: develop auto-lint

pytest:
	@$(PYTEST) --doctest-modules --doctest-glob='*.rst'

test: develop pytest

run-coverage:
	@$(COVERAGE) run -m pytest --doctest-modules --doctest-glob='*.rst'
	@$(COVERAGE) report
	@$(COVERAGE) html

coverage: develop run-coverage
	@xdg-open htmlcov/index.html

test-all:
	@$(TOX)

tox: develop test-all