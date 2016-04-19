from flask import Blueprint

machine_learning = Blueprint('machine_learning', __name__, template_folder='templates')

from app.machine_learning import events, routes
