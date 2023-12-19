# ToDo API

Этот проект представляет собой простое Django API для управления задачами в стиле ToDo.

## Начало работы

Эти инструкции помогут вам настроить и запустить проект локально.

### Предварительные требования

- Python (версия 3.6 и выше)
- Virtualenv (необязательно, но рекомендуется)

### Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/ваше_имя_пользователя/ToDo-API.git
    cd ToDo-API
    ```

2. Создайте виртуальное окружение (необязательно, но рекомендуется):

    ```bash
    virtualenv venv
    source venv/bin/activate  # На Windows: venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции:

    ```bash
    python manage.py migrate
    ```

### Запуск API

```bash
python manage.py runserver

Документация API (Swagger)

Изучите и тестируйте API с помощью Swagger:

    Swagger UI: http://127.0.0.1:8000/swagger/

API Endpoints

    Создать задачу ToDo:
        URL: /todo/create/
        Метод: POST

    Получить все задачи ToDo:
        URL: /todo/get/
        Метод: GET

    Получить конкретную задачу ToDo:
        URL: /todo/get/<int:pk>/
        Метод: GET

    Обновить задачу ToDo:
        URL: /todo/update/<int:pk>/
        Методы: PUT, PATCH

    Удалить задачу ToDo:
        URL: /todo/delete/<int:pk>/
        Метод: DELETE

