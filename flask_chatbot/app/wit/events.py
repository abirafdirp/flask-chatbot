from flask_socketio import emit

from flask import session

from app import socketio
from app.wit.wit_ai import client


@socketio.on('message', namespace='/wit')
def receive_message(message):
    bot_response = client.run_actions('mysession', str(message['data']), {})
    ans = session['answer']
    emit('response', {'data': ans})
