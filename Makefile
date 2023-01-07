MYPY_DIRS := $(shell find functions layer ! -path '*.egg-info*' -type d -maxdepth 1 -mindepth 1 | xargs)
ARTIFACTS_DIR ?= build

.PHONY: test
test:
	pytest


cleanfull: clean clean-python

.PHONY: clean
clean:
	rm -rf env
	rm -rf local
	rm -rf .aws-sam

.PHONY: clean-python
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

.PHONY: mypy
mypy: $(MYPY_DIRS)
	$(foreach d, $(MYPY_DIRS), python -m mypy $(d);)

.PHONY: develop
develop:
	python -m pip install --editable .
	python -m pip install -U -r requirements-dev.txt

.PHONY: build
build:
	rm -rf dist || true
	python -m build -w

.PHONY: build_layer
build_layer: build 
	rm -rf "$(ARTIFACTS_DIR)/python" || true
	mkdir -p "$(ARTIFACTS_DIR)/python"
	python -m pip install \
		--platform manylinux2014_x86_64 \
		--implementation cp \
		--python-version 3.9 \
		--only-binary=:all: --upgrade \
		-r requirements.txt -t "$(ARTIFACTS_DIR)/python"
	python -m pip install dist/*.whl -t "$(ARTIFACTS_DIR)/python"  

.PHONY: package_layer
package_layer: build_layer
	cd "$(ARTIFACTS_DIR)"; zip -rq ../layer.zip python

.PHONY: build-ServerlessProjectLayer
build-ServerlessProjectLayer: build_layer
