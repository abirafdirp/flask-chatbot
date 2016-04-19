from flask import session, redirect, url_for, render_template, request
from . import main


@main.route('/')
def index():
    return render_template('index.html')