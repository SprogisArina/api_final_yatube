# api_final
<<<<<<< HEAD
api final
    
=======

**Yatube** - это блог-сервис, который позволяет зарегистрироваться, создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

>Через REST API для проекта Yatube могут работать мобильное приложение, чат-бот или передаваться данные для SPA.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:SprogisArina/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

Обновить pip и установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Некоторые примеры запросов к API


### Создание публикации:

```
POST /api/v1/posts/
```

Пример данных:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Получение комментариев:

```
GET /api/v1/posts/{post_id}/comments/
```

Пример ответа:

```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

### Редактирование комментария:

```
PUT /api/v1/posts/{post_id}/comments/{id}/
```

Пример данных:

```
{
  "text": "string"
}
```

Пример ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Подписка:

```
POST /api/v1/follow/
```

Пример данных:

```
{
  "following": "string"
}
```

Пример ответа:

```
{
  "user": "string",
  "following": "string"
}
```
>>>>>>> e59239631aa0fe0909ec3fcd6efbfc83b120baf4
