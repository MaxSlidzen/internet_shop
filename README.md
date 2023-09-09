# internet_shop
Tasks on module 6

<h3>Для корректной работы необходимо:</h3>

- Установить виртуальное окружение и зайти в него;
- Установить зависимости из requirements.txt `pip3 install -r requirements.txt` или pyproject.toml `poetry install`;
- Создать в корне проекта файл `.env` и внести свои настройки проекта;
- Создать базу данных с именем "catalog";
- Применить все миграции командой `python3 manage.py migrate`;
- Создать суперпользователя для работы в админке `python3 manage.py csu`;
- Заполнить базу данных из catalog.json командой `python3 manage.py fill_db`.

<h3>Примечания:</h3>

- Создавать и редактировать продукты может только авторизованный пользователь;
- Создавать и редактировать статьи может любой пользователь;
- Сброс пароля возможен только на странице профиля;
- При удалении товара происходит редирект на страницу товаров категории удаленного продукта;
- При смене активной версии продукта происходит автоматическое сохранение выбранной версии в качестве активной