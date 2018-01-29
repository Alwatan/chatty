from flask import session, flash,redirect,url_for,render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')
