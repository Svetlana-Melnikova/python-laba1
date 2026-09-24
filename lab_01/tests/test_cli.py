"""Тесты для CLI."""

import subprocess
import sys


def _run_cli(args: list[str]) -> subprocess.CompletedProcess[str]:
    """Запустить toolkit CLI и вернуть результат.

    Args:
        args: Список аргументов командной строки (без "python -m toolkit").

    Returns:
        Объект CompletedProcess с полями stdout, stderr, returncode.
    """
    import os

    env = os.environ.copy()
    env["PYTHONPATH"] = "src"

    return subprocess.run(
        [sys.executable, "-m", "toolkit", *args],
        capture_output=True,
        text=True,
        env=env,
    )


def test_cli_calc_simple_expression() -> None:
    """python -m toolkit calc "2 + 3" печатает 5.0."""
    result = _run_cli(["calc", "2 + 3"])
    assert result.returncode == 0
    assert "5.0" in result.stdout


def test_cli_convert_cm_to_m() -> None:
    """python -m toolkit convert 100 --from cm --to m печатает 1.0."""
    result = _run_cli(["convert", "100", "--from", "cm", "--to", "m"])
    assert result.returncode == 0
    assert "1.0" in result.stdout


def test_cli_calc_error_returns_code_2() -> None:
    """Ошибочная команда calc возвращает код 2 и пишет в stderr."""
    result = _run_cli(["calc", "2 +"])
    assert result.returncode == 2
    assert result.stderr != ""
