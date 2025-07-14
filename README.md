# Django Employee Application

A simple Django CRUD application to manage employee records.

## Features

- Create, Read, Update, Delete employee records
- Bootstrap-based UI with crispy forms
- SQLite database

## Setup Instructions

```bash
git clone https://github.com/zubair-ahmad-beigh/Django-Employee-application.git
cd Django-Employee-application
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
