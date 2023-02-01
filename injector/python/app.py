from common import DIR_INJECTOR, DEBUG, MAX_ATTEMPTS, UID
from execute import execute_app
from log import log


import logging, os, requests, time


logging.basicConfig(level=logging.DEBUG)


def request_fault():
    """
    url = 'http://www.google.com'
    headers = {'Content-type': 'text/html; charset=UTF-8'}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        raise AssertionError
    if not response.status_code == 200:
        raise Exception
    print(response)
    """
    return ''


def execute_fault(fault):
    execute_app('backprop', '')


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
