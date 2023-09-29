# Укорачиватель ссылок
Укорачиватель ссылок, на котором показывается количество переходов по той или иной ссылке

## Описание
Укорачиватель ссылок созданный с использованием микрофреймворка Flask

## Технологии
* Python
* Flask
* WTForms
* SQLAlchemy

## Как запустить
1. Склонируйте репозиторий
2. Создайте и активируйте виртуальное окружение
```commandline
python -m venv venv
source venv/Scripts/activate (для Windows)
source venv/bin/activate (для Linux)
```
3. Установите зависимости
```commandline
pip install -r requirements.txt
```
4. Создайте файл .env и укажите ваш секретный ключ
```commandline
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```
5. Перейдите в директорию app и запустите flask приложение
```commandline
cd app/
flask run
```
