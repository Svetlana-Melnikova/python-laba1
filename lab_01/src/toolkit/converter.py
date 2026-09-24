"""Модуль конвертации единиц измерения."""

from toolkit.errors import ConversionError


# Группы единиц. Ключ — единица, значение — название группы.
_UNIT_TO_GROUP: dict[str, str] = {
    "mm": "length",
    "cm": "length",
    "m": "length",
    "km": "length",
    "g": "mass",
    "kg": "mass",
    "c": "temperature",
    "f": "temperature",
    "k": "temperature",
}

# Коэффициенты для перевода в базовую единицу.
# Для length базовая — метр, для mass — грамм.
# Для temperature здесь ничего нет: там нужны формулы.
_UNIT_TO_FACTOR: dict[str, float] = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "g": 1.0,
    "kg": 1000.0,
}

def _get_group(unit: str) -> str:
    """Вернуть название группы для единицы измерения.

    Args:
        unit: Название единицы, например "cm" или "KM".

    Returns:
        Название группы: "length", "mass" или "temperature".

    Raises:
        ConversionError: Если единица неизвестна.
    """
    unit_lower = unit.lower()
    if unit_lower not in _UNIT_TO_GROUP:
        raise ConversionError(f"Неизвестная единица: {unit}")
    return _UNIT_TO_GROUP[unit_lower]


def _to_base(value: float, unit: str) -> float:
    """Перевести значение в базовую единицу группы.

    Для length базовая единица — метр.
    Для mass базовая единица — грамм.
    Для temperature функция не работает.

    Args:
        value: Число, которое нужно перевести.
        unit: Единица измерения, например "km" или "g".

    Returns:
        Число в базовой единице группы.

    Raises:
        ConversionError: Если единица из группы temperature.
    """
    unit_lower = unit.lower()
    group = _get_group(unit_lower)

    if group == "temperature":
        raise ConversionError(
            "Для температуры используется отдельный перевод"
        )

    factor = _UNIT_TO_FACTOR[unit_lower]
    return value * factor


def _from_base(value: float, unit: str) -> float:
    """Перевести значение из базовой единицы в указанную.

    Для length базовая единица — метр.
    Для mass базовая единица — грамм.
    Для temperature функция не работает.

    Args:
        value: Число в базовой единице группы.
        unit: Единица, в которую нужно перевести, например "km" или "g".

    Returns:
        Число в указанной единице.

    Raises:
        ConversionError: Если единица из группы temperature.
    """
    unit_lower = unit.lower()
    group = _get_group(unit_lower)

    if group == "temperature":
        raise ConversionError(
            "Для температуры используется отдельный перевод"
        )

    factor = _UNIT_TO_FACTOR[unit_lower]
    return value / factor


def _temperature_to_celsius(value: float, unit: str) -> float:
    """Перевести температуру в градусы Цельсия.

    Args:
        value: Число — температура в единице unit.
        unit: Единица температуры: "c", "f" или "k".

    Returns:
        Температура в градусах Цельсия.
    """
    unit_lower = unit.lower()

    if unit_lower == "c":
        return value
    if unit_lower == "f":
        return (value - 32) * 5 / 9
    return value - 273.15


def _temperature_from_celsius(value: float, unit: str) -> float:
    """Перевести температуру из градусов Цельсия в указанную единицу.

    Args:
        value: Температура в градусах Цельсия.
        unit: Единица, в которую нужно перевести: "c", "f" или "k".

    Returns:
        Температура в указанной единице.
    """
    unit_lower = unit.lower()

    if unit_lower == "c":
        return value
    if unit_lower == "f":
        return value * 9 / 5 + 32
    return value + 273.15


# Минимальные допустимые температуры для каждой единицы.
_ABSOLUTE_ZERO: dict[str, float] = {
    "c": -273.15,
    "f": -459.67,
    "k": 0.0,
}


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Перевести число из одной единицы измерения в другую.

    Args:
        value: Число для перевода.
        from_unit: Исходная единица, например "cm".
        to_unit: Целевая единица, например "m".

    Returns:
        Число в целевой единице, как float.

    Raises:
        ConversionError: Если единицы из разных групп или значение
            ниже абсолютного нуля.
    """
    from_lower = from_unit.lower()
    to_lower = to_unit.lower()

    from_group = _get_group(from_lower)
    to_group = _get_group(to_lower)

    if from_group != to_group:
        raise ConversionError(
            f"Несовместимые единицы: {from_unit} и {to_unit}"
        )

    if from_group == "temperature":
        minimum = _ABSOLUTE_ZERO[from_lower]
        if value < minimum:
            raise ConversionError(
                f"Температура ниже абсолютного нуля: {value} {from_unit}"
            )
        celsius = _temperature_to_celsius(value, from_lower)
        return _temperature_from_celsius(celsius, to_lower)

    base_value = _to_base(value, from_lower)
    return _from_base(base_value, to_lower)
