from flask import Flask, render_template, session, redirect, flash
from flask_bs4 import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired
import json
import sqlite3
import hashlib

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'ghjk5678$%^&*FGHJ^&*(ghj678%^&*'
date = datetime.now()

@app.route('/')
def index():
    connection = sqlite3.connect('data/source')
    cursor = connection.cursor()
    salary = cursor.fetchall()
    connection.close()
    return render_template('index.html', title='Home', data=salary,)


if __name__ == '__main__':
    app.run(debug=True)