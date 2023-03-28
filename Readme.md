Тестовое задание для участия в практикуме IT-Academy "IT-Bootcamp".

Реализован функционал между сущностями Автор и Книга:
 - создание
 - изменение
 - удаление

У Книг может быть 1 и более Авторов. Автор может иметь 0 и более книг. Книга не может существовать без Автора и удаляется вместе с её последним Автором.

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

### 1. Create and activate virtual local-environment. Installing packages

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

### 2. Set global environment variables
```bash
cd src/
``` 
```bash
cp .env-example .env
```

### 3. Start applications
```bash
python manage.py makemigrations
``` 
```bash
python manage.py migrate
``` 
```bash
python manage.py test
``` 
```bash
python manage.py runserver
``` 
###  4. For using the app just type 127.0.0.1:8000 in yout browser.
