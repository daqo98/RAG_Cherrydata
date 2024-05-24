# RAG Cherrydata Backend - Django

Retrieval Augmented Generation is used to -> [WIP]: Maybe I'll have to change the name.

This backend was made in Django and Django Rest Framework using Clickhouse ([WIP] migration to sqlite)  as the DBMS for the backend, and Clickhouse for the analytical queries on the provided datasets.

## Requirements
Python 3.11 (Ubuntu: Install it using pyenv), pip, pipenv, clickhouse-server ([follow the steps to install the binary](https://clickhouse.com/docs/en/getting-started/quick-start#1-download-the-binary))

## Setup
1. Create the Python environment using Pipfile. Do this by going to the project folder and run `pipenv install`.
2. Once the installation has finished, enter the shell of the environment `pipenv shell`.

## Clickhouse DB setup
Create a folder called "clickhouse", install the binary and run it..

## Celery - Async task processing
Follow this tutorial: [https://realpython.com/asynchronous-tasks-with-django-and-celery/].

1. Install a message broker e.g. Redis or RabbitMQ. Let's use Redis [https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/linux/]. Version used: redis-stack-server_7.2.0-v10_amd64.deb.

## Web App

1. In order to build the models, run:
    * `python manage.py makemigrations`
    * Apply the migrations: `python manage.py migrate` and `python manage.py migrate --database clickhouse`.

2. To run the server: `python manage.py runserver`.

3. To explore the database view open the admin view pane:
    a. Create a superuser: `python manage.py createsuperuser`.
    b. Go to `http://127.0.0.1:8000/admin/` and log in using the credentials set previously.


## Execution 

Run the Clickhouse binary, the redis-server, the Django's web app development server, and Celery all of them in separate terminal shells:

```
./clickhouse server
redis-server
python manage.py runserver
python -m celery -A RAG_Cherrydata worker -l info
```

You need to restart the Celery worker every time you modify the task code because it loads it into memory.

## Endpoints
Check the [Postman collection](RAG_Cherrydata.postman_collection.json) for examples. 
[WIP] [Swagger][https://swagger.io/] 