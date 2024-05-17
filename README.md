# RAG Cherrydata Backend - Django

Retrieval Augmented Generation is used to .

This backend was made in Django and Django Rest Framework using PostgreSQL as the DBMS for the backend, and Clickhouse for the analytical queries on the provided datasets.

## Requirements
Python 3.11 (Ubuntu: Install it using pyenv), pip, pipenv

## Setup
1. Create the Python environment using Pipfile. Go to the project folder and run `pipenv install`.

2. Enter the shell of the environment `pipenv shell`.

## Execution

1. In order to build the models, run:
* `python manage.py makemigrations`
* Apply the migrations: `python manage.py migrate` and `python manage.py migrate --database clickhouse`.

2. To run the server: `python manage.py runserver`.

3. To explore the database view open the admin view pane: `http://127.0.0.1:8000/admin/`

## Clickhouse DB setup


## Celery - Async task processing
Follow this tutorial: [https://realpython.com/asynchronous-tasks-with-django-and-celery/].

1. Install a message broker e.g. Redis or RabbitMQ. Let's use Redis [https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/linux/]. Version used: redis-stack-server_7.2.0-v10_amd64.deb.

2. In a terminal window run `redis-server`.
3. In another terminal run `redis-cli` and on it run `ping`.


Run the Django's web app development server, the redis-server and Celery:

```
python manage.py runserver
redis-server 
python -m celery -A RAG_Cherrydata worker
python -m celery -A RAG_Cherrydata worker -l info
```
You need to restart the Celery worker every time you modify the task code because it loads it into memory.

## Endpoints
[WIP] [Swagger][https://swagger.io/] 