from flask import session, redirect, url_for, render_template, request
from app.main import main


@main.route('/wit-ai')
def chat_wit():
    return render_template('wit_ai.html')