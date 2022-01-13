# MyIITJ-auth
Authentication API for MYIITJ app

### Purpose

Authentication for the MYIITJ app with Auth2.0

### Installation:

Requirements:

- Python 3 runtime
- Django >= 3.2.9
- Other dependencies in `Pipfile`

Procedure:

Make sure you have python 3 and pipenv installed on your pc.

Then follow these steps:

```
cd <project-directory>/

cp .env.example .env
```

```
pipenv install --dev
```

- Activate the new virtual environment:

```
pipenv shell
```

- cd to the src directory

```
cd src/
```

- Make database migrations

```
python manage.py makemigrations
python manage.py migrate
```

- Create a superuser

```
python manage.py createsuperuser
```

- Run development server on localhost

```
python manage.py runserver
```

#### Dummy Data for Testing [OPTIONAL]:

This will populate the database with random values for testing:

```
python manage.py createfixture
```