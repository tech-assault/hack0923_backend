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
![django version](https://img.shields.io/badge/Django-4.1-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.14-green)



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


### Документация к API доступна по адресу

**api/docs/**

#### Документация API доступна по адресам:
```sh
http://127.0.0.1:8000/api/schema/swagger-ui/
```
```sh
http://127.0.0.1:8000/api/schema/redoc/
```
#### Админка доступна по адресу:

```sh
http:/localhost/admin/
```



## Команда

- [Марина Балахонова](https://github.com/margoloko)
- [Павел Зияев](https://github.com/p0lzi)

___
