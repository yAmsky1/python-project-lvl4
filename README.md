### Hexlet tests and linter status:
[![Actions Status](https://github.com/yAmsky1/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/yAmsky1/python-project-lvl4/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b4a10a79be8b3aeeaa53/maintainability)](https://codeclimate.com/github/yAmsky1/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b4a10a79be8b3aeeaa53/test_coverage)](https://codeclimate.com/github/yAmsky1/python-project-lvl4/test_coverage)
[![Linter](https://github.com/yamsky1/python-project-lvl2/actions/workflows/ci.yml/badge.svg)](https://github.com/yamsky1/python-project-lvl4/actions/workflows/ci.yml)

## Task-manager
#### Task Manager is a web application for task management. In this application, you have the ability to create tasks, statuses, tags. For each task, you can specify one status, one or more labels, the executor. You can also make changes to tasks, change the executor, etc.

###### App at [Heroku](https://dry-reaches-00803.herokuapp.com)

### Installing via poetry:

#### clone:

```git clone https://github.com/yamsky1/python-project-lvl4```

```cd python-project-lvl4```

#### install dependencies:

```make install```

### Usage:

##### You need create a ".env" file in the app root directory and list there local vars:

``` SECRET_KEY='your_secret_key' ```

``` ACCESS_TOKEN='rollbar_access_token' ```

##### set ```DEBUG=Yes```, if you want to enable debug mode.

#### Creating and applying migrations based on models
```make migrations```
#### Running the application on a local server
```make run-server```

##### starts at http://127.0.0.1:8000/

### Installation:

`pip install --user git+https://github.com/yamsky1/python-project-lvl4`

#### Install dependencies:
```pip install -r requirements.txt```

### Usage:
You need create a ".env" file in the app root directory and list there local vars:

``` SECRET_KEY='your_secret_key' ```

``` ACCESS_TOKEN='rollbar_access_token' ```

#### set ```DEBUG=Yes```, if you want to enable debug mode.


#### Creating and applying migrations based on models
```python manage.py makemigrations```

```python manage.py migrate```


#### Running the application on a local server

``` python manage.py runserver ```

##### starts at http://127.0.0.1:8000/


### USED:
- #### Web-framework - Django
- #### Localization - i18n
- #### Tests - Django unittest 
- #### Python dependency management - Poetry
- #### CI/CD - Github Actions
- #### Linter - flake8
- #### Cloud application platform - Heroku
- #### Error-tracking - Rollbar

