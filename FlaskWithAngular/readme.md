# Notes
These are my notes from a blog about [Flask with Angular](https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/)

## Issues
The blog post uses `.data`, such as `new_exam = ExamSchema().dump(exam).data`, but that throws an AttributeError error for me: `AttributeError: 'dict' object has no attribute 'data'`, so I deleted all of those and then it works. Environmental differences? Version differences? I suspect it's related to Marshmallow (it seems it used to return a (data, errors) tuple, but since v3.0.0b7 it just returns serialised data).


# Setup notes
## Sample Docker DB
Sample -- obviously change the username/password ... but honestly I think I'll just use SQLite for now.
```
docker run --name online-exam-db \
    -p 5432:5432 \
    -e POSTGRES_DB=online-exam \
    -e POSTGRES_PASSWORD=0NLIN3-ex4m \
    -d postgres
```

## Sample curl calls for Windows
### POST
`curl -X POST -H "Content-Type: application/json" -d "{ \"title\": \"TypeScript Advanced Exam\", \"description\": \"Tricky questions about TypeScript.\" }" http://127.0.0.1:5000/exams`

### GET
`curl http://127.0.0.1:5000/exams`

## Node.js and NPM
Fetch from [nodejs.org](https://nodejs.org/en/download/)

and then install the Angular CLI: `npm install -g @angular/cli`.
Angular analytics can be switched off again with `ng analytics off`.

### Angular initialisation
The Angular CLI is executed with `ng`, for instance to create a new `frontend` folder: `ng new frontend`, which creates the basic structure of an Angular app.  
Use `--skip-git` to omit the auto-creation of a git repository.


Link frontend to backend by:
- navigate to `./frontend/src/app`
- create a file called `env.ts`
- with contents `export const API_URL = 'http://localhost:5000';`
*can also be enhanced to support different environments*

Due to issues with TypeScript 3.7+, I had to add to `tsconfig.json` a compiler option to `"skipLibCheck": true`.

Due to import issues, I had to use `npm i @angular/material@7.3.2 @angular/cdk hammerjs` instead of `npm i @angular/material @angular/cdk hammerjs`

#### Running the frontend
Navigate to `.frontend` and serve it with `ng serve`, it'll he available on `http://localhost:4200`.

Sometimes CTRL+C doesn't seem to stop it, then use `netstat -ano | findstr :4200` to find the PID (upper right) and `taskkill /PID {PID} /F` to kill it.

#### Tweaks
Needed to manually install the `rxjs-compat` package to avoid a linting error, inside the `frontend` folder run: `npm install rxjs-compat --save`.

Needed to add type to the `.get()` call, i.e. ```.get(`${API_URL}/exams`)``` -> ```.get<Exam[]>(`${API_URL}/exams`)```.


## Pipenv
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

## CORS
Cross-Origin Resource Sharing (CORS) is needed otherwise most browsers will block requests to the API. See [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

Without any further configuration, flask-cors allows CORS for all domains on all routes:
```
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
```

[flask-cors can be further tweaked](http://flask-cors.readthedocs.io/en/latest/#resource-specific-cors)

## Auth0 Auth call for Windows
```
curl --request POST --url https://dev-3-5kafu4.eu.auth0.com/oauth/token --header "content-type: application/json" --data "{\"client_id\":\"m8pEtq22nmxIV24YFVhsWBJTrscfjxJl\",\"client_secret\":\"{client_secret}\",\"audience\":\"https://FlaskWithAngular.antra.dk\",\"grant_type\":\"client_credentials\"}"
```