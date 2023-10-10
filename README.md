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

# Кратко о работе DS и разработчиков

backend:


frontend:
- Язык JavaScript
- Написан на библиотеке React
- Реализована статика приложения в соответствии с дизайном
- Рализовано взаимодействие с api в асинхронной стилистике с применением axios

ds:
- Выполнена предобработка исходных данных
- Проведен исследовательский анализ данных
- Сгенерированы новые признаки для обучения модели на основании выявленных зависимостей
- Для предсказания разработана модель LGBMClassifier, подобраны оптимальные гиперпараметры
- Проведено тестирование, в результате которого получены метрики F1_macro и Accuracy
- Создан API сервер на FastAPI для взаимодействия по REST API


# Запуск проекта локально (По порядку)

- Переходим в корневую директорию проекта (Y_Hackathon_1/)
- В файле docker-compose.yml указать .env переменные (Изначально - подставлены переменные по умолчанию с целью упрощённого запуска. На боевом сервере убрать в Git secrets)
- Запустить демон Docker
- Находясь в терминале в директории (Y_Hackathon_1/) выполнить команду "docker-compose up -d"

# После успешного запуска будут заняты соответствующие порты на localhost
- http://localhost:8000/docs (Документация backend)
- http://localhost:8001/docs (Документация yandex mock server)
- http://localhost:8002/docs (Документация сервера DS)
- http://localhost/ (Полноценное приложение (frontend))


## Команда

- [Марина Балахонова](https://github.com/margoloko)
- [Павел Зияев](https://github.com/p0lzi)

___
