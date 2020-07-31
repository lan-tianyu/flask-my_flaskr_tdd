import os
from functools import wraps
from flask import (Flask, request, session, redirect, url_for, abort,
                   render_template, flash, jsonify)
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = b'\x14l\x86x\x0eD\x9f\xa8\x03\x07S\x1b9G\xe4\x16'
USERNAME = 'admin'
PASSWORD = 'admin'
SQLAlCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL", f'sqlite:///{os.path.join(basedir, "flaskr.db")}')
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

import models


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash("Please login")
            return jsonify({"status": 0, "message": "Please login"}), 401
    return 



@app.route("/")
def index():
    entries = db.session.query(models.Flaskr)
    return render_template('index.html', entries=entries)


@app.route("/add", methods=['POST']
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    new_entry = models.Flaskr(request.form['title'], request.form['content'])
    db.session.add(new_entry)
    db.session.commit()
    flash('New entry was successful posted')
    return redirect(url_for('index'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config.get('USERNAME'):
            error = 'Invalid username'
        elif request.form['password'] != app.config.get('PASSWORD'):
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in')
    flash('You were logged out')
    return redirect(url_for('index'))


@app.route('/delete/<int:post_id>', methods=["GET"])
@login_required
def delete_entry(post_id):
    result = {"status": 0, "message": "Error"}
    try:
        new_id = post_id
        db.session.query(models.Flaskr).filter_by(post_id=new_id).delete()
        db.session.commit()
        result = {"status": 1, "message": "Post Deleted"}
    except Exception as e:
        result = {"status": 0, "message": repr(e)}
    return jsonify(result)


@app.route('/search', methods=["GET"])
def search():
    query = request.args.get("query")
    entries = db.session.query(models.Flaskr)
    if query:
        return render_template("search.html", entries=entries, query=query)
    return render_template('search.html')



if __name__ == '__main__':
    app.run()