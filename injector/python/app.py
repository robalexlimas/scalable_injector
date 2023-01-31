from common import DIR_INJECTOR, DEBUG, UID
from log import log
from responses import response


from flask import Flask
from flask_cors import CORS
import logging, os, time


logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def entry():
    return response('Hello from API')


if __name__ == '__main__':
    while True:
        try:
            app.run(debug=DEBUG, host='0.0.0.0', port=3000)
        except:
            logging.exception('Error in main loop')
            logging.error('Waiting 10s and restarting')
            log('Error in main loop')
            time.sleep(10)

