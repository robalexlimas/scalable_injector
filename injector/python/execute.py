from common import APPS


import logging, os, signal, subprocess, time


logging.basicConfig(level=logging.DEBUG)


def execute_app(app_script, fault):
    logging.info('Running app: {} with fault: {}'.format(
        app_script.split('/')[-1],
        fault.split(',')[0]
    ))
    process = subprocess.Popen(
        app_script, 
        shell=True, 
        executable='/bin/bash',
        preexec_fn=os.setsid
    )
    [timeout, code] = is_timeout(process, 10)


def is_timeout(process, time):
    total_time = time.time() + time
    while True:
        code = process.poll()
        if code is not None:
            return [False, code]
        time_now = time.time()
        if time_now > total_time:
            os.killpg(process.pid, signal.SIGINT)
            logging.warning('Timeout')
            return [True, code]
        time.sleep(1)
