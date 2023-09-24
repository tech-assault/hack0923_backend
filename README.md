# Проект «DemandOracle»


### Краткое описание проекта

Главное задача проекта прогнозирование спроса 


### **Стек**

![python version](https://img.shields.io/badge/Python-3.7-green)
![django version](https://img.shields.io/badge/Django-2.2-green)
![djangorestframework version](https://img.shields.io/badge/DRF-3.12-green)


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
docker-compose exec backend python manage.py migrate       
```

Создать суперпользователя

```
docker-compose exec backend python manage.py createsuperuser   
```    

Собрать статику

``` 
docker-compose exec backend python manage.py collectstatic --no-input 
```   


### Документация к API доступна по адресу

**api/docs/**


## Команда

- [Марина Балахонова](https://github.com/margoloko)
- [Павел Зияев](https://github.com/p0lzi)

___ 

