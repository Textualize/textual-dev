from click.testing import CliRunner
from importlib.metadata import version

from textual_dev.cli import run


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(run, ["--version"])
    assert version("textual") in result.output
