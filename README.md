# internet_shop
Tasks on module 6

Для корректной работы необходимо:
- В settings.py ввести свой пароль от postgresql;
- Создать базу данных с именем "catalog";
- Установить виртуальное окружение и зайти в него;
- Установить зависимости из requirements.txt (pip3 install -r requirements.txt) или pyproject.toml (poetry install);
- Применить все миграции командой python3 manage.py migrate
- Создать суперпользователя для работы в админке (python3 manage.py createsuperuser);
- Заполнить базу данных из catalog.json командой python3 manage.py fill_db


