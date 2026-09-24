"""Модуль валидации списка токенов."""

from toolkit.errors import CalculationError



def _is_binary_operator(token_type: str) -> bool:
    """Проверить, является ли тип токена бинарным оператором.

    Args:
        token_type: Тип токена, например "PLUS" или "NUMBER".

    Returns:
        True, если это бинарный оператор, иначе False.
    """
    return (
        token_type == "PLUS"
        or token_type == "MINUS"
        or token_type == "STAR"
        or token_type == "SLASH"
    )



def _validate(tokens: list[tuple]) -> None:
    """Проверить корректность списка токенов.

    Args:
        tokens: Список токенов после токенизации.

    Returns:
        None. Функция ничего не возвращает.

    Raises:
        CalculationError: Если список токенов некорректен.
    """
    if len(tokens) == 0:
        raise CalculationError("Пустое выражение")
    first_token_type = tokens[0][0]

    if first_token_type == "PLUS" or first_token_type == "MINUS" or first_token_type == "STAR" or first_token_type == "SLASH":
        raise CalculationError(
            "Выражение не может начинаться с бинарного оператора"
        )

    last_token_type = tokens[-1][0]
    if (
        last_token_type == "PLUS"
        or last_token_type == "MINUS"
        or last_token_type == "STAR"
        or last_token_type == "SLASH"
        or last_token_type == "UNARY_PLUS"
        or last_token_type == "UNARY_MINUS"
    ):
        raise CalculationError(
            "Выражение не может заканчиваться оператором"
        )

    for i in range(1, len(tokens)):
        prev_type = tokens[i - 1][0]
        curr_type = tokens[i][0]
        if _is_binary_operator(prev_type) and _is_binary_operator(curr_type):
            raise CalculationError(
                "Два бинарных оператора подряд"
            )
