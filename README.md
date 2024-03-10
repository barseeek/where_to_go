# Where to Go
Сайт про интересные места Москвы на карте


## Установка и запуск

1. Клонируйте репозиторий:
    ```
    git clone https://github.com/barseeek/where_to_go.git
    ```
2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
3. Создайте файл `.env` со следующими параметрами:

   ```ini
   SECRET_KEY=секретный ключ
   DEBUG=False или Truе 
   ALLOWED_HOSTS=ваши разрешенные адреса
   STATIC_ROOT=путь к статике для продакшена
   DATABASE_ENGINE=система хранения
   DATABASE_NAME=имя базы
   DJANGO_LOG_LEVEL=уровень логгирования
   DJANGO_LOG_FILE=путь к файлу 
   ```

4. Запустите миграции:

   ```bash
   python manage.py migrate
   ```

5. Создайте суперпользователя Django:

   ```bash
   python manage.py createsuperuser
   ```

6. Запустите сервер:

   ```bash
   python manage.py runserver
   ```

## Загрузка новых данных из JSON
Для того чтобы создать новый объект на карте из JSON файла можно воспользоваться командой `load_place` с обязательным параметром `-u/-url`.
Например,
```bash
python manage.py load_place -u https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
```
Пример JSON файла можно найти по [ссылке](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).