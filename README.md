# Установка
1. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate 
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Примените миграции:
```
python manage.py migrate
```
4. Создайте суперпользователя (опционально):
```
python manage.py createsuperuser
```
5. Запустите сервер разработки:
```
python manage.py runserver
```
Откройте [http://127.0.0.1:8000](http://127.0.0.1:8000) в браузере.

