"""Модуль калькулятора арифметических выражений."""

from toolkit.errors import CalculationError
from toolkit.tokenizer import _tokenize
from toolkit.validator import _validate



# Приоритеты операторов: чем больше число, тем выше приоритет.
_OPERATOR_PRIORITY: dict[str, int] = {
    "PLUS": 1,
    "MINUS": 1,
    "STAR": 2,
    "SLASH": 2,
    "UNARY_MINUS": 3,
    "UNARY_PLUS": 3,
}


def _to_rpn(tokens: list[tuple]) -> list[tuple]:
    """Перевести токены из обычной записи в обратную польскую нотацию.

    Args:
        tokens: Список токенов в обычной записи.

    Returns:
        Список токенов в обратной польской нотации.
    """
    output: list[tuple] = []
    stack: list[tuple] = []

    for token in tokens:
        token_type = token[0]
        if token_type == "NUMBER":
            output.append(token)
            continue

        if token_type == "PLUS" or token_type == "MINUS" or token_type == "STAR" or token_type == "SLASH":
            while len(stack) > 0 and _OPERATOR_PRIORITY[stack[-1][0]] >= _OPERATOR_PRIORITY[token_type]:
                output.append(stack.pop())
            stack.append(token)
            continue

        if token_type == "UNARY_MINUS" or token_type == "UNARY_PLUS":
            stack.append(token)
            continue

    while len(stack) > 0:
        output.append(stack.pop())

    return output


def _calculate_rpn(rpn: list[tuple]) -> float:
    """Вычислить результат по списку токенов в ОПН.

    Args:
        rpn: Список токенов в обратной польской нотации.

    Returns:
        Результат вычисления, как float.

    Raises:
        CalculationError: Если деление на ноль или ошибка в структуре.
    """

    stack: list[float] = []

    for token in rpn:
        token_type = token[0]
        if token_type == "NUMBER":
            stack.append(token[1])
            continue

        if token_type == "PLUS":
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)
            continue

        if token_type == "MINUS":
            right = stack.pop()
            left = stack.pop()
            stack.append(left - right)
            continue

        if token_type == "STAR":
            right = stack.pop()
            left = stack.pop()
            stack.append(left * right)
            continue

        if token_type == "SLASH":
            right = stack.pop()
            left = stack.pop()
            if right == 0:
                raise CalculationError("Деление на ноль")
            stack.append(left / right)
            continue

        if token_type == "UNARY_MINUS":
            value = stack.pop()
            stack.append(-value)
            continue
        if token_type == "UNARY_PLUS":
            continue

    return stack[0]



def evaluate(expr: str) -> float:
    """Вычислить арифметическое выражение.

    Args:
        expr: Строка с выражением, например "2 + 3 * 4".

    Returns:
        Результат вычисления, как float.

    Raises:
        CalculationError: Если выражение некорректно.
    """
    tokens = _tokenize(expr)
    _validate(tokens)
    rpn = _to_rpn(tokens)
    return _calculate_rpn(rpn)
