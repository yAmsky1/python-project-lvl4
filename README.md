### Hexlet tests and linter status:
[![Actions Status](https://github.com/yAmsky1/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/yAmsky1/python-project-lvl4/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/b4a10a79be8b3aeeaa53/maintainability)](https://codeclimate.com/github/yAmsky1/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b4a10a79be8b3aeeaa53/test_coverage)](https://codeclimate.com/github/yAmsky1/python-project-lvl4/test_coverage)

## Task-manager

###### App at [Heroku](https://dry-reaches-00803.herokuapp.com)

### Installation:

`pip install --user git+https://github.com/yamsky1/python-project-lvl4`

### Usage:
You need create a ".env" file in the root directory and list there local vars:

``` SECRET_KEY='your_secret_key' ```

``` ACCESS_TOKEN='rollbar_access_token' ```

set ```DEBUG=Yes```, if you want to enable debug mode.

### Running the application on a local server

``` make run-server ```

starts at http://127.0.0.1:8000/
