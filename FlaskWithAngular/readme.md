# Notes
These are my notes from a blog about [Flask with Angular](https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/)

## Sample Docker DB
Sample -- obviously change the username/password ... but honestly I think I'll just use SQLite for now.
```
docker run --name online-exam-db \
    -p 5432:5432 \
    -e POSTGRES_DB=online-exam \
    -e POSTGRES_PASSWORD=0NLIN3-ex4m \
    -d postgres
```

## Node.js and NPM
Fetch from [nodejs.org](https://nodejs.org/en/download/)

and then install the Angular CLI: `npm install -g @angular/cli`.
Angular analytics can be switched off again with `ng analytics off`.

# Pipenv
Trying out Pipenv for the first time (instead of venv): `pip install pipenv`.

Initialise it with: `pipenv --three`
Install in it with: `pipenv install sqlalchemy`

Run Pipenv scripts with `pipenv run -m moduleName` or `pipenv shell` (for interactive shell) followed by e.g.: `python -m src.main`

Aborted -- tutorial doesn't work well on my windows machine. Will go back to venv:
```
venv\scripts\activate
SET FLASK_APP=src/main
flask run
```