"""Тесты для модуля calculator."""

import pytest

from toolkit.calculator import evaluate
from toolkit.errors import CalculationError


def test_evaluate_simple_addition() -> None:
    """2 + 3 = 5."""
    assert evaluate("2 + 3") == 5.0


def test_evaluate_simple_subtraction() -> None:
    """10 - 4 = 6."""
    assert evaluate("10 - 4") == 6.0


def test_evaluate_simple_multiplication() -> None:
    """3 * 4 = 12."""
    assert evaluate("3 * 4") == 12.0


def test_evaluate_simple_division() -> None:
    """10 / 2 = 5."""
    assert evaluate("10 / 2") == 5.0


def test_evaluate_priority_multiplication() -> None:
    """2 + 3 * 4 = 14 (умножение раньше сложения)."""
    assert evaluate("2 + 3 * 4") == 14.0


def test_evaluate_priority_division() -> None:
    """10 - 6 / 2 = 7."""
    assert evaluate("10 - 6 / 2") == 7.0


def test_evaluate_left_associativity() -> None:
    """10 - 3 - 2 = 5 (вычитание слева направо)."""
    assert evaluate("10 - 3 - 2") == 5.0


def test_evaluate_unary_minus() -> None:
    """-5 * 2 = -10."""
    assert evaluate("-5 * 2") == -10.0


def test_evaluate_double_unary_minus() -> None:
    """--5 = 5 (минус от минуса)."""
    assert evaluate("--5") == 5.0


def test_evaluate_floats() -> None:
    """3.5 + 1.5 = 5."""
    assert evaluate("3.5 + 1.5") == 5.0


def test_evaluate_long_expression() -> None:
    """Длинное выражение с несколькими операциями."""
    assert evaluate("2 + 3 * 4 - 10 / 2") == 9.0


def test_evaluate_empty_expression() -> None:
    """Пустое выражение — ошибка."""
    with pytest.raises(CalculationError):
        evaluate("")


def test_evaluate_invalid_character() -> None:
    """Недопустимый символ — ошибка."""
    with pytest.raises(CalculationError):
        evaluate("2 @ 3")


def test_evaluate_two_operators_in_a_row() -> None:
    """Два бинарных оператора подряд — ошибка."""
    with pytest.raises(CalculationError):
        evaluate("2 + * 3")


def test_evaluate_ends_with_operator() -> None:
    """Выражение заканчивается оператором — ошибка."""
    with pytest.raises(CalculationError):
        evaluate("2 +")


def test_evaluate_division_by_zero() -> None:
    """Деление на ноль — ошибка."""
    with pytest.raises(CalculationError):
        evaluate("1 / 0")
