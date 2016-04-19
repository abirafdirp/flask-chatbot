from flask import Flask
from flask.ext.socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .main import main as main_blueprint
    from .machine_learning import machine_learning as machine_learning_blueprint
    from .wit import wit as wit_ai_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(machine_learning_blueprint)
    app.register_blueprint(wit_ai_blueprint)

    socketio.init_app(app)
    return app