# Консольное приложение для управления библиотекой книг

## Описание

Это простое консольное приложение для управления библиотекой книг. Приложение позволяет добавлять, удалять, искать, отображать книги и изменять их статус. Каждая книга содержит следующие поля:
- `id` (уникальный идентификатор, генерируется автоматически)
- `title` (название книги)
- `author` (автор книги)
- `year` (год издания)
- `status` (статус книги: “в наличии” или “выдана”)

## Функционал

1. **Добавление книги**: Пользователь вводит название, автора и год издания новой книги. Книга добавляется в библиотеку с уникальным ID и статусом "в наличии".
2. **Удаление книги**: Пользователь вводит ID книги, которую нужно удалить из библиотеки.
3. **Поиск книги**: Пользователь может искать книги по названию, автору или году издания.
4. **Отображение всех книг**: Приложение выводит список всех книг с их ID, названием, автором, годом издания и текущим статусом.
5. **Изменение статуса книги**: Пользователь вводит ID книги и новый статус ("в наличии" или "выдана"), чтобы изменить текущий статус книги.

## Структура проекта

- `main.py`: Основной скрипт, запускающий консольное приложение.
- `library.py`: Содержит класс `Library`, управляющий коллекцией книг.
- `book.py`: Содержит класс `Book`, представляющий книгу.

## Использование

### 1. Клонирование репозитория

```sh
git clone https://github.com/sulaymanovI/Library.git
cd your-repository-name
python main.py
