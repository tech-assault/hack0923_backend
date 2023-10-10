# Проект «Forecast»


### Краткое описание проекта

Главное задача проекта прогнозирование спроса для товаров собственного производства с ежедневным обновлением.

### Фунционал

- реализовано api для взаимодействия с Frontend
- реализовано импорт и экспорт данных в панель администрирование Django (с помощью библиотеки django-import-export) с возможностью оптимизации импорта и экспорта данных (django-import-export-celery)
- реализовано взаимодействия с микросервисом ML (запуск осуществляеться при каждом импорте данных в таблицу Sale)
- Написаны соответствующие тесты при помощи unittest


### **Стек**

![python version](https://img.shields.io/badge/Python-3.10-green)
![django version](https://img.shields.io/badge/Django-4.2-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.14-green)

### Оглавление:
- [Проект «Forecast»](#проект-forecast)
    - [Технологии](#стек)
    - [Оглавление:](#оглавление)
    - [Описание проекта](#краткое-описание-проекта)
    - [Запуск проекта](#как-запустить-проект)
    - [Локальный запуск проекта](#локальный-запуск-проекта)
      - [Запуск приложения на локальном сервере](#запуск-приложения-на-локальном-сервере)
      - [Адрес документации API](#документация-api-доступна-по-адресам)
      - [Адрес административной панели](#админка-доступна-по-адресу)
  - [Команда](#команда)

### Краткое описание проекта

Главное задача проекта прогнозирование спроса для товаров собственного производства с ежедневным обновлением.


### Как запустить проект:

Клонировать репозитории в одной папке в командной строке:

```
git clone https://github.com/tech-assault/hack0923_frontend.git
git clone https://github.com/tech-assault/hack0923_backend.git
git clone https://github.com/tech-assault/hack0923_ml.git
```



Перейти в папку infra репозитория hack0923_backend
```
cd hack0923_backend/infra
```

Запустить docker-compose

```
docker-compose up
```

Выполнить миграции

```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя

```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику

```
docker-compose exec web python manage.py collectstatic --no-input
```
### Локальный запуск проекта
Клонируйте реппозиторий

```
git clone https://github.com/tech-assault/hack0923_backend.git
```

Перейдите в папку с проектом hack0923_backend, установите виртуальное окружение.

```
cd hack0923_backend
```

```
python -m venv venv
```
и запустите виртуальное окружение:

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```
**Установка зависимостей**

Перейдите в папку backend и установите зависимости
  ```
cd backend
  ```
  ```
  pip install -r requirements.txt
  ```

**Применяем миграции:**

  ```
  python manage.py migrate
  ```
**Создаем суперпользователя:**

  ```
  python manage.py createsuperuser
  ```
#### Запуск приложения на локальном сервере

* Если у вас windows
    ```
    python manage.py runserver
    ```
* Если у вас Linux/MacOS
    ```
    python3 manage.py runserver
    ```
**Для запуска тестов:**

  ```
  python manage.py test
  ```
#### Документация API доступна по адресам:

```sh
http://127.0.0.1:8000/api/schema/docs/
```
#### Админка доступна по адресу:

```sh
http:/localhost/admin/
```



## Команда

- [Марина Балахонова](https://github.com/margoloko)
- [Павел Зияев](https://github.com/p0lzi)

___
