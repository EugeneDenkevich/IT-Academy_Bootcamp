Тестовое задание для участия в практикуме IT-Academy "IT-Bootcamp".

Реализован функционал между сущностями Автор и Книга:
 - создание
 - изменение
 - удаление

У Книг может быть 1 и более Авторов. Автор может иметь 0 и более книг. Книга не может существовать без Автором и удаляется вместе с её последним Автором.

Создано 2 теста на проверку валидации формы Книги.

Созданы переменные окружения.

CI/CD пайплайн реализовать не успел.

Инструкция к запуску:

# IT-Academy_Bootcamp

### 
> ### Technologies used:
>
> - Django
> - Bootstrap 5


## Pre installation

### 2. Create and activate virtual local-environment. Installing packages

###  for Windows:

```bash
python -m venv venv
```
```bash
cd venv/Scripts
```
```bash
.\activate
```
```bash
cd ../../IT-Academy_Bootcamp
```
```bash
pip install -r requirements.txt
```

###  for Linux:

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
cd IT-Academy_Bootcamp
```
```bash
pip install -r requirements.txt
```

<hr>

### 1. Set global environment variables
```bash
cd src/
``` 
```bash
cp .env-example .env
```

### Start applications
```bash
python manage.py makemigrations
``` 
```bash
python manage.py migrate
``` 
```bash
python manage.py runserver
``` 
