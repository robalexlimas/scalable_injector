import os


BASE_DIR = '/'
DIR_INJECTOR = '/injector'
DIR_APPS = os.path.join(DIR_INJECTOR, 'apps')
DIR_GPGPUSIM = os.path.join(DIR_INJECTOR, 'gpgpu-sim_distribution')
DIR_GPGPUSIM_CONFIG = os.path.join(DIR_GPGPUSIM, 'configs/tested-cfgs/')
DIR_RESULTS = os.path.join(DIR_INJECTOR, 'results')
LOG_PATH = os.path.join(BASE_DIR, 'log.txt')
MAX_ATTEMPTS = 10


APPS = {
    'backprop': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'backprop'),
        'binary': 'run',
        'args': '2048'
    },
    'gaussian': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'gaussian'),
        'binary': 'run',
        'args': '16'
    },
    'nn': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'nn'),
        'binary': 'run',
        'args': os.path.join(DIR_APPS, 'rodinia', 'data', 'nn', 'list640k_64.txt')
    },
    'lavamd': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'lavaMD'),
        'binary': 'run',
        'args': '2'
    },
    'lud': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'lud'),
        'binary': 'run',
        'args': '256'
    },
    'heartwall': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'heartwall'),
        'binary': 'run',
        'args': '{} 2'.format(os.path.join(DIR_APPS, 'rodinia', 'data', 'heartwall', 'test.avi'))
    },
    'cfd': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'cfd'),
        'binary': 'run',
        'args': os.path.join(DIR_APPS, 'rodinia', 'data', 'cfd', 'fvcorr.domn.097K')
    }
}
