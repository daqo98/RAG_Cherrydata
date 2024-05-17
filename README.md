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

## Endpoints
[WIP] [Swagger][https://swagger.io/] 