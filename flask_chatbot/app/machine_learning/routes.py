from flask import session, redirect, url_for, render_template, request
from app.main import main


@main.route('/machine-learning')
def chat_chatterbot():
    return render_template('machine_learning.html')