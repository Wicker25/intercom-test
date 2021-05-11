import pytest

from click.testing import CliRunner

from cli import command


def test_command():
    runner = CliRunner()
    result = runner.invoke(command, ['--dataset=dataset/customers.txt', '--max-distance=30.0'])

    assert result.exit_code == 0
    assert result.output == """[user_id=4] Ian Kehoe
[user_id=5] Nora Dempsey
[user_id=6] Theresa Enright
"""
