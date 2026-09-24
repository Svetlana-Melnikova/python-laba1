"""Модуль токенизации арифметических выражений."""

from toolkit.errors import CalculationError



def _is_valid_number(number_str: str) -> bool:
    """Проверить, является ли строка корректным числом.

    Args:
        number_str: Строка, которую проверяем, например "12" или "3.14".

    Returns:
        True, если строка — корректное число, иначе False.
    """
    digits_only = number_str.replace(".", "")
    return digits_only.isdigit() and digits_only != ""



def _tokenize(expr: str) -> list[tuple]:
    """Разбить строку выражения на список токенов.

    Args:
        expr: Строка с арифметическим выражением, например "2 + 3 * 4".

    Returns:
        Список токенов. Каждый токен — кортеж:
        ("NUMBER", value) для числа или ("PLUS",) для оператора.

    Raises:
        CalculationError: Если встретился недопустимый символ.
    """
    tokens: list[tuple] = []
    number_str: str = ""
    previous_was_number: bool = False


    for char in expr:
        if char == " ":
            continue

        if char.isdigit() or char == ".":
            number_str = number_str + char
            continue

        if number_str != "":
            if not _is_valid_number(number_str):
                raise CalculationError(
                    f"Неверное числовое значение: {number_str}"
                )
            tokens.append(("NUMBER", float(number_str)))
            number_str = ""
            previous_was_number = True

        if char == "+":
            if previous_was_number:
                tokens.append(("PLUS",))
            else:
                tokens.append(("UNARY_PLUS",))
            previous_was_number = False
            continue

        if char == "-":
            if previous_was_number:
                tokens.append(("MINUS",))
            else:
                tokens.append(("UNARY_MINUS",))
            previous_was_number = False
            continue

        if char == "*":
            tokens.append(("STAR",))
            previous_was_number = False
            continue

        if char == "/":
            tokens.append(("SLASH",))
            previous_was_number = False
            continue

        raise CalculationError(
            f"Недопустимый символ: {char}"
        )

    if number_str != "":
        if not _is_valid_number(number_str):
            raise CalculationError(
                f"Неверное числовое значение: {number_str}"
            )
        tokens.append(("NUMBER", float(number_str)))

    return tokens
