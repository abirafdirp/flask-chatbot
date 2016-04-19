from wit import Wit
from flask import session


def say(session_id, context, msg):
    print(msg)
    session['answer'] = msg


def merge(session_id, context, entities, msg):
    return context


def error(session_id, context, e):
    print(str(e))

actions = {
    'say': say,
    'merge': merge,
    'error': error,
}

client = Wit('RIXBHE3PJMYKAVLJQPPULB7AQ5VOSYYL', actions)
