"""Кастомные исключения для пакета toolkit."""


class ToolkitError(Exception):
    """Базовое исключение для всех ошибок пакета toolkit."""


class CalculationError(ToolkitError):
    """Ошибка при вычислении арифметического выражения."""


class ConversionError(ToolkitError):
    """Ошибка при конвертации величин."""
