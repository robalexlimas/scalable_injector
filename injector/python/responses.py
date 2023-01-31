
from flask import make_response, jsonify


def response(message, data=None, status=200):
    res = {'message': message, 'data': data} if data else {'message': message}
    return make_response(jsonify(res), status)


def error(message, status=400):
    return response(message, status=status)
