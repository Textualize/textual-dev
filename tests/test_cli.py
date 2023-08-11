from click.testing import CliRunner
from importlib_metadata import version

from textual_dev.cli import run


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(run, ["--version"])
    assert version("textual") in result.output


def test_cli_keys():
    runner = CliRunner()
    result = runner.invoke(run, ["keys"])
    assert result.exit_code == 0
