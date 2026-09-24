"""Тесты для модуля converter."""

import pytest

from toolkit.converter import convert
from toolkit.errors import ConversionError


def test_convert_cm_to_m() -> None:
    """100 см = 1 м."""
    assert convert(100.0, "cm", "m") == 1.0


def test_convert_m_to_cm() -> None:
    """1 м = 100 см."""
    assert convert(1.0, "m", "cm") == 100.0


def test_convert_km_to_m() -> None:
    """1 км = 1000 м."""
    assert convert(1.0, "km", "m") == 1000.0


def test_convert_mm_to_cm() -> None:
    """10 мм = 1 см."""
    assert convert(10.0, "mm", "cm") == 1.0


def test_convert_kg_to_g() -> None:
    """1 кг = 1000 г."""
    assert convert(1.0, "kg", "g") == 1000.0


def test_convert_g_to_kg() -> None:
    """2000 г = 2 кг."""
    assert convert(2000.0, "g", "kg") == 2.0


def test_convert_celsius_to_fahrenheit() -> None:
    """25 °C = 77 °F."""
    assert convert(25.0, "c", "f") == 77.0


def test_convert_fahrenheit_to_celsius() -> None:
    """32 °F = 0 °C."""
    assert convert(32.0, "f", "c") == 0.0


def test_convert_celsius_to_kelvin() -> None:
    """0 °C = 273.15 K."""
    assert convert(0.0, "c", "k") == 273.15


def test_convert_case_insensitive() -> None:
    """Регистр не важен: CM = cm."""
    assert convert(100.0, "CM", "M") == 1.0


def test_convert_incompatible_groups() -> None:
    """Нельзя перевести сантиметры в килограммы."""
    with pytest.raises(ConversionError):
        convert(5.0, "cm", "kg")


def test_convert_unknown_unit() -> None:
    """Неизвестная единица — ошибка."""
    with pytest.raises(ConversionError):
        convert(5.0, "xyz", "m")


def test_convert_below_absolute_zero() -> None:
    """Температура ниже абсолютного нуля — ошибка."""
    with pytest.raises(ConversionError):
        convert(-300.0, "c", "k")
