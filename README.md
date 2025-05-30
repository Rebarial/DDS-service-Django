## DDS-service-Django
Для запуска приложения необходим python 3.0+ и пакетный менеджер pip

```bash

git clone https://github.com/Rebarial/DDS-service-Django

cd DDS-service-Django

```
По желанию создайте виртуальное окружение

Windows:
```bash
python -m venv venv

venv\Scripts\activate
```

Linux/macOS:
```bash
python3 -m venv venv

source venv/bin/activate
```

Установите зависимости.

```bash
pip install -r requirements.txt
```

Запускаем проект
```bash
python app/manage.py runserver 
```

В качестве бд использовался sqlite3. Файл базы данных добавлен в проект и настройки не требуется.

Смотрим результат:
http://localhost:8000/

При необходимости можно выполнить миграции
```bash
python app/manage.py makemigrations dds_service
python app/manage.py migrate
```
