# Notes
These are notes from playing around with Flask, based on a [Youtube video](https://www.youtube.com/watch?v=MwZwr5Tvyxo).

## Running Flask
- set environmental variable FLASK_APP to whatever python file holds the site (e.g. set/export FLASK_APP=flaskblog.py)
- enable debug mode by setting FLASK_DEBUG=1 (avoids restarting the webserver to display changes)
- run the flask webserver with "flask run"
- Alternatively, add the classic if __name__ == '__main__': app.run(debug=True) to the python file

## Basic boilerplate stuff
- Initial commit has a basic shell with the bootstrap layout
- Generate a nice secret key with the Python module 'secrets', e.g.:
```
>>> import secrets
>>> secrets.token_hex(16)
'f198558879180bd328e1df1f5812ec6f'
```



# Refactor at some point
- Add the flask-bootstrap extension; should help with the Forms/Validation quirkiness