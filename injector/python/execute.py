from common import APPS, DIR_APPS, DIR_INJECTOR, DIR_GPGPUSIM, UID
from config_gpgpusim import load_params


import logging, os, signal, subprocess, time


logging.basicConfig(level=logging.DEBUG)


def execute_app_with_fault(app_name, fault):
    app_dir = APPS[app_name]['dir']
    app_script = APPS[app_name]['binary']
    args = APPS[app_name]['args']
    timeout = APPS[app_name]['timeout']
    logging.info(
        'Running app: {} with fault: {}'.format(
            app_name,
            'test'
        )
    )
    load_params(app_dir, fault)
    process = execute_app(app_name, app_dir, app_script, args, timeout, False)
    [timeout, code] = is_timeout(process, timeout)


def execute_golden_app(app_name):
    app_dir = APPS[app_name]['dir']
    app_script = APPS[app_name]['binary']
    args = APPS[app_name]['args']
    timeout = APPS[app_name]['timeout']
    logging.info('Running app: {}'.format(app_name))
    load_params(app_dir)
    process = execute_app(app_name, app_dir, app_script, args, timeout)
    process.wait()


def execute_app(app_name, app_dir, app_script, args, timeout, golden=True):
    commands = '{} {} {} {}'.format(
        '{}/{}'.format(app_dir, app_script),    # route executable
        DIR_GPGPUSIM,                           # route gpgpu-sim
        app_dir,                                # route app
        args                                    # args to execute
    )
    logging.info('Command: {}'.format(commands))
    results_dir = os.path.join(DIR_INJECTOR, 'results', UID)
    exits_dir(results_dir)
    output_name = '{}_golden.txt'.format(app_name) if golden else '{}.txt'.format(app_name)
    output_result = os.path.join(results_dir, output_name)
    with open(output_result, 'w') as file:
        process = subprocess.Popen(
            commands, 
            shell=True, 
            executable='/bin/bash',
            preexec_fn=os.setsid,
            stdout=file
        )
    return process


def is_timeout(process, time_exe):
    total_time = time.time() + time_exe
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


def exits_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
