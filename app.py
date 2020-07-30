import os
from functools import wraps
from flask import (
    Flask, 
    request,
    session,
    redirect,
    url_for,
    abort,
    render_template,
    flash,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = b'\x14l\x86x\x0eD\x9f\xa8\x03\x07S\x1b9G\xe4\x16'
USERNAME = 'admin'
PASSWORD = 'admin'
SQLAlCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f'sqlite:///{os.path.join(basedir, "flaskr.db")}')
SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)



if __name__ == '__main__':
    app.run()