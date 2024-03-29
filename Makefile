#############################################################################
# Common make values.
.DEFAULT_GOAL := help
package       := textual_dev
run           := poetry run
python        := $(run) python
pytest        := $(run) pytest
lint          := $(run) pylint
mypy          := $(run) mypy
black         := $(run) black
isort         := $(run) isort
textual       := $(python) -m $(package)

##############################################################################
# Setup/update/repo admin targets.
.PHONY: setup
setup:				# Set up the development environment for the tool
	poetry install
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
	$(black) src/$(package) tests/

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

.PHONY: test
test:				# Run the unit tests.
	$(pytest) tests/

.PHONY: checkall
checkall: lint stricttypecheck test	# Check all the things

##############################################################################
# The main interfaces for the package (for easy in-development testing).
.PHONY: textual
textual:			# Show the help for the textual command.
	$(textual)

.PHONY: borders
borders:			# Show the Textual borders preview.
	$(textual) borders

.PHONY: colors
colors:			# Show the Textual colours preview.
	$(textual) colors

.PHONY: console
console:			# Run the textual console
	$(textual) console

.PHONY: diagnose
diagnose:			# Run the Textual diagnosis tool.
	$(textual) diagnose

.PHONY: easing
easing:			# Run the Textual easing preview.
	$(textual) easing

.PHONY: keys
keys:				# Run the Textual keys tool.
	$(textual) keys

.PHONY: run
run:				# Test the textual run command.
	$(textual) run

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
