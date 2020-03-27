import os
from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import BookmarkForm

basedir = os.path.abspath(os.path.dirname(__file__))

# from logging import DEBUG

app = Flask(__name__)
# app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '\x8e\t\xfa}\xea\xfc\xd2\x82\xa3\xb8\x91\xf2n8\xc2\xef}\xf9\xa1\xb3@x\xeb\x9a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'thermos.db')
db = SQLAlchemy(app)


bookmarks = []


def store_bookmark(url, description):
    bookmarks.append(dict(
        url=url,
        description=description,
        user="antra",
        date=datetime.utcnow()
    ))


def new_bookmarks(num):
    # return the last <num> bookmarks sorted by date
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title="Title passed from view to template",
                           text="Text passed from view to template",
                           user=User("Anders", "Demant van der Weide"),
                           new_bookmarks=new_bookmarks(5))


# This is the original "add" with a basic form input, which didn't have "Description"
@app.route('/add_old', methods=['GET', 'POST'])
def add_old():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url, description="")
        #app.logger.debug('stored url: ' + url)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')


# This is the updated "add" using WTForms
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    # If method=GET OR form-content is invalid, then...
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash("Stored bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
