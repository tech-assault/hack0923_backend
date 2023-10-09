# Проект «Forecast»


### Краткое описание проекта

Главное задача проекта прогнозирование спроса для товаров собственного производства с ежедневным обновлением.


### **Стек**

![python version](https://img.shields.io/badge/Python-3.10-green)
![django version](https://img.shields.io/badge/Django-4.1-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.14-green)


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/tech-assault/hack0923_backend.git
```

Перейти в папку infra
```
cd /infra
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
http://127.0.0.1:8000/api/schema/docs/
```
#### Админка доступна по адресу:

```sh
http://127.0.0.1:8000/admin/
```

### Установка pre-commit hooks

Для того, чтобы при каждом коммите выполнялись pre-commit проверки, необходимо:
- Установить pre-commit
- Установить pre-commit hooks

#### Установка pre-commit
Модуль pre-commit уже добавлен в requirements и должен установиться автоматически с виртуальным окружением.

Проверить установлен ли pre-commit можно командой (при активированном виртуальном окружении):
```sh
pre-commit --version
>> pre-commit 3.3.3
```

Если этого не произошло, то необходимо установить pre-commit:
```sh
pip install pre-commit
```

#### Установка hooks
Установка хуков:
```sh
pre-commit install --all
```
Установка хука для commitizen
```sh
pre-commit install --hook-type commit-msg
```
В дальнейшем, при выполнении команды git commit будут выполняться проверки, перечисленные в файле .pre-commit-config.yaml.

Если не видно, какая именно ошибка мешает выполнить commit, можно запустить хуки вручную командой:
```sh
pre-commit run --all-files
```

### Работа с commitizen
Чтобы сгенерировать установленный git-commit, запустите в вашем терминале
```sh
cz commit
```
или сочетание клавиш
```sh
cz c
```

## Команда

- [Марина Балахонова](https://github.com/margoloko)
- [Павел Зияев](https://github.com/p0lzi)

___
