from click.testing import CliRunner
from importlib.metadata import version

from textual_dev.cli import run


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(run, ["--version"])
    assert version("textual") in result.output


# def test_cli_widgets():
#     runner = CliRunner()
#     result = runner.invoke(run, ["widgets"])
#     assert result.exit_code == 0


def test_cli_diagnose():
    runner = CliRunner()
    result = runner.invoke(run, ["diagnose"])
    assert result.exit_code == 0


def test_cli_keys():
    runner = CliRunner()
    result = runner.invoke(run, ["keys"])
    assert result.exit_code == 0
