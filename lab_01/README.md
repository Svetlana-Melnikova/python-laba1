# Лабораторная работа 1. Консольный набор утилит

**Автор:** Мельникова Светлана

## Описание

Python-пакет `toolkit` с CLI, содержащий:
- **калькулятор** арифметических выражений,
- **конвертер** единиц измерения (длина, масса, температура).

## Установка

```
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

## Использование

### Калькулятор

```
python -m toolkit calc "2 + 3 * 4"
```

Результат: `14.0`

```
python -m toolkit calc "-5 * 2"
```

Результат: `-10.0`

Поддерживаемые операции: `+`, `-`, `*`, `/`, унарные `+` и `-`.

Приоритет операций: `*` и `/` выполняются раньше `+` и `-`.

### Конвертер

```
python -m toolkit convert 100 --from cm --to m
```

Результат: `1.0`

```
python -m toolkit convert 25 --from c --to f
```

Результат: `77.0`

Поддерживаемые группы единиц:

- **длина:** `mm`, `cm`, `m`, `km`
- **масса:** `g`, `kg`
- **температура:** `c`, `f`, `k`

Регистр не учитывается. Конвертация между разными группами запрещена.

### Справка

```
python -m toolkit --help
```

## Структура проекта

```
lab_01/
├── pyproject.toml
├── README.md
├── src/
│   └── toolkit/
│       ├── __init__.py
│       ├── __main__.py
│       ├── tokenizer.py
│       ├── validator.py
│       ├── calculator.py
│       ├── converter.py
│       └── errors.py
└── tests/
    ├── test_tokenizer.py
    ├── test_validator.py
    ├── test_calculator.py
    ├── test_converter.py
    └── test_cli.py
```

## Тесты

```
cd lab_01
python -m pytest
```

## Требования

- Python 3.9+
- pytest
