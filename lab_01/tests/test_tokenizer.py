"""Тесты для модуля tokenizer."""

import pytest

from toolkit.errors import CalculationError
from toolkit.tokenizer import _tokenize


def test_tokenize_single_number() -> None:
    """Одно число превращается в один токен."""
    tokens = _tokenize("5")
    assert tokens == [("NUMBER", 5.0)]


def test_tokenize_simple_addition() -> None:
    """Выражение "2 + 3" даёт три токена."""
    tokens = _tokenize("2 + 3")
    assert tokens == [
        ("NUMBER", 2.0),
        ("PLUS",),
        ("NUMBER", 3.0),
    ]


def test_tokenize_float_number() -> None:
    """Число с точкой распознаётся как одно число."""
    tokens = _tokenize("3.14")
    assert tokens == [("NUMBER", 3.14)]


def test_tokenize_negative_number() -> None:
    """-5 превращается в унарный минус и число."""
    tokens = _tokenize("-5")
    assert tokens == [
        ("UNARY_MINUS",),
        ("NUMBER", 5.0),
    ]


def test_tokenize_no_spaces() -> None:
    """Пробелы не нужны: "2+3" и "2 + 3" — одинаково."""
    tokens = _tokenize("2+3")
    assert tokens == [
        ("NUMBER", 2.0),
        ("PLUS",),
        ("NUMBER", 3.0),
    ]


def test_tokenize_ignores_spaces() -> None:
    """Лишние пробелы игнорируются."""
    tokens = _tokenize("  2   +   3  ")
    assert tokens == [
        ("NUMBER", 2.0),
        ("PLUS",),
        ("NUMBER", 3.0),
    ]


def test_tokenize_invalid_character() -> None:
    """Символ @ — недопустимый."""
    with pytest.raises(CalculationError):
        _tokenize("2 @ 3")


def test_tokenize_dot_only() -> None:
    """Одна точка — не число."""
    with pytest.raises(CalculationError):
        _tokenize(".")
