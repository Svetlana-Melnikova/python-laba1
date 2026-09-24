"""Тесты для модуля validator."""

import pytest

from toolkit.errors import CalculationError
from toolkit.validator import _validate


def test_validate_simple_expression() -> None:
    """Правильное выражение не бросает ошибок."""
    tokens = [("NUMBER", 2.0), ("PLUS",), ("NUMBER", 3.0)]
    _validate(tokens)


def test_validate_single_number() -> None:
    """Одно число — валидное выражение."""
    tokens = [("NUMBER", 5.0)]
    _validate(tokens)


def test_validate_unary_minus_ok() -> None:
    """Унарный минус в начале — это НЕ ошибка."""
    tokens = [("UNARY_MINUS",), ("NUMBER", 5.0)]
    _validate(tokens)


def test_validate_unary_in_middle_ok() -> None:
    """Бинарный + унарный — это НЕ два бинарных, ошибки нет."""
    tokens = [
        ("NUMBER", 2.0),
        ("STAR",),
        ("UNARY_MINUS",),
        ("NUMBER", 3.0),
    ]
    _validate(tokens)


def test_validate_empty_tokens() -> None:
    """Пустой список — ошибка."""
    with pytest.raises(CalculationError):
        _validate([])


def test_validate_starts_with_binary_operator() -> None:
    """Выражение не может начинаться с бинарного оператора."""
    tokens = [("STAR",), ("NUMBER", 5.0)]
    with pytest.raises(CalculationError):
        _validate(tokens)


def test_validate_ends_with_operator() -> None:
    """Выражение не может заканчиваться оператором."""
    tokens = [("NUMBER", 2.0), ("PLUS",)]
    with pytest.raises(CalculationError):
        _validate(tokens)


def test_validate_two_binary_operators() -> None:
    """Два бинарных оператора подряд — ошибка."""
    tokens = [
        ("NUMBER", 2.0),
        ("PLUS",),
        ("STAR",),
        ("NUMBER", 3.0),
    ]
    with pytest.raises(CalculationError):
        _validate(tokens)
