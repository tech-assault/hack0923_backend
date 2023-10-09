# Проект «Forecast»

### Стек

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
    - [Установка pre-commit hooks](#установка-pre-commit-hooks)
      - [Установка pre-commit](#установка-pre-commit)
      - [Установка hooks](#установка-hooks)
      - [Работа с commitizen](#работа-с-commitizen)
  - [Команда](#команда)

### Краткое описание проекта

Главное задача проекта прогнозирование спроса для товаров собственного производства с ежедневным обновлением.

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

#### Работа с commitizen
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
