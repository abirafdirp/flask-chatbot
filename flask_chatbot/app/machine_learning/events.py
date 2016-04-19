from flask_socketio import emit
from chatterbot import ChatBot

from app import socketio

chatbot = ChatBot('swdev',
                  logic_adapters=[
                      'chatterbot.adapters.logic.EvaluateMathematically',
                      'chatterbot.adapters.logic.TimeLogicAdapter',
                      'chatterbot.adapters.logic.ClosestMatchAdapter'
                  ])
chatbot.train('chatterbot.corpus.english')
chatbot.train('chatterbot.corpus.english.greetings')
chatbot.train('chatterbot.corpus.english.conversations')


@socketio.on('message', namespace='/machinelearning')
def receive_message(message):
    bot_response = chatbot.get_response(message['data'])
    emit('response', {'data': bot_response})
