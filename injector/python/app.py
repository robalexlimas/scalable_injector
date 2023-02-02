from common import APPS, DIR_INJECTOR, DEBUG, MAX_ATTEMPTS
from execute import execute_golden_app, execute_app_with_fault
from log import log


import json, logging, os, requests, time


logging.basicConfig(level=logging.DEBUG)


def request_fault():
    url = 'http://controller/fault'
    headers = {'Content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    content = json.loads(response.content)
    logging.info('Response. {}'.format(content))
    if response.status_code == 404:
        raise AssertionError
    if not response.status_code == 200:
        raise Exception
    return {
        'app': content['data']['app'],
        'fault': content['data']['fault']
    }


def execute_fault(fault):
    app, fault_info = fault['app'], fault['fault']
    if len(fault_info) > 0:
        execute_app_with_fault(app, fault_info)
    else:
        execute_golden_app(app)


if __name__ == '__main__':
    while True:
        try:
            fault = request_fault()
            execute_fault(fault)
        except AssertionError:
            logging.exception('Fault list complete')
        except Exception:
            logging.exception('Server down')
        finally:
            time.sleep(10)
