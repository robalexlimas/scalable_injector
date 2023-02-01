import os, uuid


BASE_DIR = os.getcwd()
DIR_INJECTOR = os.path.join(os.getcwd(), '..')
DIR_APPS = os.path.join(DIR_INJECTOR, 'apps')
DIR_GPGPUSIM = os.path.join(DIR_INJECTOR, 'gpgpu-sim_distribution')
DIR_GPGPUSIM_CONFIG = os.path.join(DIR_GPGPUSIM, 'configs/tested-cfgs/SM75_RTX2060')
# DEBUG = str(os.getenv('DEBUG')).startswith('1')
DEBUG = True
LOG_PATH = os.path.join(BASE_DIR, 'log.txt')
MAX_ATTEMPTS = 10
UID = uuid.uuid1()


APPS = {
    'backprop': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'backprop'),
        'binary': 'run',
        'args': '65536',
        'timeout': 10
    },
    'gaussian': {
        'dir': '',
        'binary': '',
        'args': '',
        'timeout': 10
    },
    'nn': {
        'dir': '',
        'binary': '',
        'args': '',
        'timeout': 10
    },
    'lavamd': {
        'dir': '',
        'binary': '',
        'args': '',
        'timeout': 10
    },
    'lu': {
        'dir': '',
        'binary': '',
        'args': '',
        'timeout': 10
    },
    'heartwall': {
        'dir': '',
        'binary': '',
        'args': '',
        'timeout': 10
    },
    'cfd': {
        'dir': '',
        'binary': '',
        'args': '',
        'timeout': 10
    }
}
