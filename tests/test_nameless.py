
from click.testing import CliRunner

from nameless.cli import main
import nameless


def test_main():
    assert 'site-packages' in nameless.__file__
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
