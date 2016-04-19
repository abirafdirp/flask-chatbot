from flask import Blueprint

wit = Blueprint('wit', __name__, template_folder='templates')

from app.wit import events, routes
