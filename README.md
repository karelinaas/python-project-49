[![asciicast](https://asciinema.org/a/InujH91XAFI1jfxj.svg)](https://asciinema.org/a/InujH91XAFI1jfxj)

### Hexlet tests and linter status:
[![Actions Status](https://github.com/karelinaas/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/karelinaas/python-project-49/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=karelinaas_python-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=karelinaas_python-project-49)

# Brain Games

Набор консольных игр для тренировки математических навыков и логического мышления.

## Описание проекта

Brain Games - это коллекция из пяти обучающих игр, которые помогают развивать математические способности:

- **Even Game** - определение четности числа
- **Calc Game** - решение простых арифметических выражений
- **GCD Game** - нахождение наибольшего общего делителя
- **Progression Game** - поиск пропущенного элемента в арифметической прогрессии
- **Prime Game** - определение простого числа

## Минимальные требования

- Python 3.13 или выше
- Установленный пакетный менеджер [uv](https://docs.astral.sh/uv/)

## Инструкции по установке

1. Клонируйте репозиторий:
```bash
git clone https://github.com/karelinaas/python-project-49.git
cd python-project-49
```

2. Установите зависимости:
```bash
make install
# или
uv sync
```

## Инструкции по запуску

### Запуск конкретных игр

```bash
# Игра на определение четности
brain-even

# Калькулятор
brain-calc

# Наибольший общий делитель
brain-gcd

# Арифметическая прогрессия
brain-progression

# Простые числа
brain-prime
```

### Сборка проекта

```bash
make build
# или
uv build
```

### Проверка кода

```bash
make lint
# или
uv run ruff check brain_games
```
