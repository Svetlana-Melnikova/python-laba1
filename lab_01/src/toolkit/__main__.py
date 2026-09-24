"""Точка входа CLI для пакета toolkit."""

import argparse
import sys

from toolkit.calculator import evaluate
from toolkit.converter import convert
from toolkit.errors import CalculationError, ConversionError



def _build_parser() -> argparse.ArgumentParser:
    """Собрать и вернуть парсер аргументов командной строки.

    Returns:
        Настроенный ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Калькулятор и конвертер единиц измерения.",
    )
    subparsers = parser.add_subparsers(dest="command")

    calc_parser = subparsers.add_parser(
        "calc",
        help="Вычислить арифметическое выражение.",
    )

    calc_parser.add_argument(
        "expression",
        help="Выражение, например '2 + 3 * 4'.",
    )
    convert_parser = subparsers.add_parser(
        "convert",
        help="Перевести значение из одной единицы в другую.",
    )
    convert_parser.add_argument(
        "value",
        type=float,
        help="Число для перевода.",
    )
    convert_parser.add_argument(
        "--from",
        dest="from_unit",
        required=True,
        help="Исходная единица, например 'cm'.",
    )
    convert_parser.add_argument(
        "--to",
        dest="to_unit",
        required=True,
        help="Целевая единица, например 'm'.",
    )

    return parser


def _run_calc(expression: str) -> int:
    """Вычислить выражение и напечатать результат.

    Args:
        expression: Строка с выражением.

    Returns:
        Код возврата: 0 при успехе.
    """
    result = evaluate(expression)
    print(result)
    return 0


def _run_convert(value: float, from_unit: str, to_unit: str) -> int:
    """Перевести значение и напечатать результат.

    Args:
        value: Число для перевода.
        from_unit: Исходная единица.
        to_unit: Целевая единица.

    Returns:
        Код возврата: 0 при успехе.
    """
    result = convert(value, from_unit, to_unit)
    print(result)
    return 0

def main() -> int:
    """Запустить CLI.

    Returns:
        Код возврата: 0 при успехе, 2 при ошибке.
    """
    parser = _build_parser()
    args = parser.parse_args()

    try:
        if args.command == "calc":
            return _run_calc(args.expression)
        if args.command == "convert":
            return _run_convert(args.value, args.from_unit, args.to_unit)
    except (CalculationError, ConversionError) as error:
        print(error, file=sys.stderr)
        return 2

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
