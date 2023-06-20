#############################################################################
# Common make values.
.DEFAULT_GOAL := help
package       := textual_dev
run           := poetry run
python        := $(run) python
lint          := $(run) pylint
mypy          := $(run) mypy
black         := $(run) black
isort         := $(run) isort

##############################################################################
# Setup/update/repo admin targets.
.PHONY: setup
setup:				# Set up the development environment for the tool
	poetry install --extras dev
	$(run) pre-commit install

.PHONY: relock
relock:			# Rebuild the lock file.
	poetry lock

.PHONY: update
update:			# Update the development environment
	poetry update

##############################################################################
# Reformatting tools.
.PHONY: black
black:				# Run black over the code
	$(black) src/$(package)

.PHONY: isort
isort:				# Run isort over the code
	$(isort) --profile black src/$(package)

.PHONY: reformat
reformat: isort black		# Run all the formatting tools over the code

##############################################################################
# Checking/testing/linting/etc.
.PHONY: lint
lint:				# Run Pylint over the library
	$(lint) src/$(package)

.PHONY: typecheck
typecheck:			# Perform static type checks with mypy
	$(mypy) --scripts-are-modules src/$(package)

.PHONY: stricttypecheck
stricttypecheck:	        # Perform strict static type checks with mypy
	$(mypy) --scripts-are-modules --strict src/$(package)

.PHONY: checkall
checkall: lint stricttypecheck	# Check all the things

##############################################################################
# The main interfaces for the package (for easy in-development testing).
.PHONY: console
console:			# Run the textual console
	$(python) -m $(package)

.PHONY: borders
borders:			# Show the Textual borders preview.
	$(python) -m $(package) borders

##############################################################################
# Utility.
.PHONY: repl
repl:				# Start a Python REPL
	$(python)

.PHONY: shell
shell:				# Create a shell within the virtual environment
	poetry shell

.PHONY: help
help:				# Display this help
	@grep -Eh "^[a-z]+:.+# " $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.+# "}; {printf "%-20s %s\n", $$1, $$2}'

##############################################################################
# Housekeeping tasks.
.PHONY: housekeeping
housekeeping:			# Perform some git housekeeping
	git fsck
	git gc --aggressive
	git remote prune origin
	git remote update --prune
