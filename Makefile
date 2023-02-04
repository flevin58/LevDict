ifndef VIRTUAL_ENV
$(error The Virtual Environment is not active!)
endif

MODULE=levdict

define HELP
Available commands are:\n
\tbuild\t\tBuilds a new version (remember to update version in toml)\n
\tupload\t\tUploads the new version to PiPy\n
\ttest_upload\tUploads the new version to Test PiPy\n
\ttest_install\tInstalls from Test PiPy\n
\tinstall\t\tInstalls from PiPy\n
endef
export HELP

SOURCES = $(wildcard ./src/$(MODULE)/*.py)
DISTROS = $(wildcard ./dist/*)

update:
	python -m pip install --upgrade pip
	python -m pip install --upgrade build
	python -m pip install --upgrade twine

build:
	python -m build

test_upload:
	python -m twine upload --repository testpypi dist/*

test_install:
	python -m pip install -i https://test.pypi.org/project/ $(MODULE)

upload:
	python -m twine upload dist/*

install:
	python -m pip install $(MODULE)

dev_install:
	python -m pip install --editable .

help:
	@echo $$HELP
