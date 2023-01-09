MYPY_DIRS := $(shell find functions layer ! -path '*.egg-info*' -type d -maxdepth 1 -mindepth 1 | xargs)
ARTIFACTS_DIR ?= build

# testing
test:
	pytest

mypy: $(MYPY_DIRS)
	$(foreach d, $(MYPY_DIRS), python -m mypy $(d);)

.PHONY: test mypy

# clean project
clean:
	rm -rf env
	rm -rf local
	rm -rf .aws-sam

clean-python:
	rm -rf **/.pytest_cache
	rm -rf .tox
	rm -rf dist
	rm -rf build
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	rm -rf .coverage*

cleanfull: clean clean-python

.PHONY: clean clean-python cleanfull

# development
.PHONY: develop
develop:
	python -m pip install --editable .
	python -m pip install -U -r requirements-dev.txt

# build project
build-shared:
	rm -rf dist || true
	python -m build -w

build-ServerlessProjectLayer: build-shared
	rm -rf "$(ARTIFACTS_DIR)/python" || true
	mkdir -p "$(ARTIFACTS_DIR)/python"
	python -m pip install dist/*.whl -t "$(ARTIFACTS_DIR)/python"  

build-ServerlessDependenciesLayer:
	rm -rf "$(ARTIFACTS_DIR)/python" || true
	mkdir -p "$(ARTIFACTS_DIR)/python"
	python -m pip install \
		--platform manylinux2014_x86_64 \
		--implementation cp \
		--python-version 3.9 \
		--only-binary=:all: --upgrade \
		-r requirements.txt -t "$(ARTIFACTS_DIR)/python"

.PHONY: build-shared build-ServerlessProjectLayer build-ServerlessDependenciesLayer build-fast
