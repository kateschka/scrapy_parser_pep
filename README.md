# Парсер документов PEP

## Описание

Парсер документации PEP на базе фреймворка Scrapy. Собирает информацию о PEP (Python Enhancement Proposals) с сайта https://peps.python.org/ и формирует сводную таблицу статусов документов.

## Технологии

- Python 3.9
- Scrapy 2.5
- CSV

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/scrapy_parser_pep.git
cd scrapy_parser_pep
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Запустите парсер:

```bash
scrapy crawl pep
```

## Результаты

После выполнения парсера в директории `results` будут созданы два файла:

- `pep_[timestamp].csv` - содержит информацию о всех PEP (номер, название, статус)
- `status_summary_[timestamp].csv` - содержит сводную информацию по статусам PEP

## Тестирование

Для запуска тестов используйте команду:

```bash
pytest
```

Автор:
Кузнецова Екатерина
