### Локальный запуск приложения
#### Запуск контейнеров
```shell
docker stop $(docker ps -aq)
docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
```

#### Запуск миграций
```shell
docker-compose exec backend sh
python manage.py makemigrations
python manage.py migrate
```

Приложение будет доступно по адресу [http://localhost:8000/main/](http://localhost:8000/main/)  
Документация API доступна по адресу [http://localhost:8000/api/docs](http://localhost:8000/api/docs/)

----
