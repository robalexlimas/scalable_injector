from common import APPS, DIR_APPS, DIR_INJECTOR, DIR_GPGPUSIM, DIR_RESULTS
from config_gpgpusim import load_params


import logging, os, signal, subprocess, time


logging.basicConfig(level=logging.DEBUG)


def execute_app_with_fault(app_name, fault):
    app_dir = APPS[app_name]['dir']
    app_script = APPS[app_name]['binary']
    args = APPS[app_name]['args']
    timeout = APPS[app_name]['timeout']
    logging.info(
        'Fault: SM {}, SM sub core {}, core type {}, core id {}, in out {}, operad {}, mask {}, stuckat {}'
        .format(
            fault['sm_id'],
            fault['sm_sub_core_id'],
            fault['core_type'],
            fault['core_id'],
            fault['in_out'],
            fault['operand'],
            fault['mask'],
            fault['stuckat']
        )
    )
    load_params(app_dir, fault)
    process = execute_app(app_name, app_dir, app_script, args, timeout, False)
    [timeout, code] = is_timeout(process, timeout)


def execute_golden_app(app_name, fault):
    app_dir = APPS[app_name]['dir']
    app_script = APPS[app_name]['binary']
    args = APPS[app_name]['args']
    timeout = APPS[app_name]['timeout']
    logging.info('Running app: {}'.format(app_name))
    load_params(app_dir, fault)
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
    exits_dir(DIR_RESULTS)
    stdout_name = '{}_golden.log'.format(app_name) if golden else '{}.log'.format(app_name)
    stderr_name = 'stderr.log'
    stdout_dir = os.path.join(DIR_RESULTS, stdout_name)
    stderr_dir = os.path.join(DIR_RESULTS, stderr_name)
    file_stdout = open(stdout_dir, 'w')
    file_stderr = open(stderr_dir, 'w')
    process = subprocess.Popen(
        commands, 
        shell=True, 
        executable='/bin/bash',
        preexec_fn=os.setsid,
        stdout=file_stdout,
        stderr=file_stderr
    )
    file_stdout.close()
    file_stderr.close()
    return process


def is_timeout(process, time_exe):
    total_time = time.time() + (1.5 * time_exe)
    while True:
        code = process.poll()
        logging.info('Code: {}'.format(code))
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
