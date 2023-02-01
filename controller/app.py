from common import error, response


from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def info():
    data = {
        'organization': 'Politecnico di Torino',
        'group': 'CAD',
        'author': 'Robert Alexander Limas Sierra'
    }
    return response('Injector', data=data)


@app.route('/fault', methods=['GET'])
def fault():
    data = {
        'fault': '',
        'app': 'backprop'
    }
    return response('Fault information', data=data)


if __name__ == '__main__':
    app.run()
