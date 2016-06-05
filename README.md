# Plex Requests API

[![Build Status](https://travis-ci.org/ccl2of4/plex-requests-api.png)](https://travis-ci.org/ccl2of4/plex-requests-api)

## Setting up virtualenv

1) Install virtualenv
  * `(sudo) pip install virtualenv`

2) Create a local virtual environment for python3 (as opposed to the default python2).
  * `virtualenv -p python3 env`
  * This will create a folder called 'env' in the current directory.

3) Your virtual environment is now set up. Activate it.
  * `. env/bin/activate`

## Installing dependencies

The file 'requirements.txt' lists all the dependencies to run the app.
  * `pip install -r requirements.txt`

The file 'test_requirements.txt' lists additional dependencies for running tests.
 * `pip install -r test_requirements.txt`

If you need to add a dependency, the easiest way to do that is
  * `pip install [dependency] && pip freeze > requirements.txt`

## Configuration

The following environment variable is required to run the app:
  * `TMDB_API_KEY`: API key for [themoviedb](https://www.themoviedb.org/)

See config.py for additional optional configuration

## Running the app

Run the script as an executable
  * `./run.py`
Alternatively, run using python
  * `python run.py`

## Running functional tests

To run the functional tests, first configure the server to use the same database
that the tests will be using. Each test wipes the database before running. Then
run the server

* Set db environment variable for both server and tests `export DB_PATH='test_requests.db'`
* Run all tests `py.test functional_tests`
* Run single test `py.test functional_tests/[test_name.py]`

## Swagger

If the app is run locally using default configuration the Swagger GUI will be visible at <http://localhost:5000/api>
