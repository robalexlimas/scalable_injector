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
        'verify': 'verify',
        'args': '2048'
    },
    'gaussian': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'gaussian'),
        'binary': 'run',
        'verify': 'verify',
        'args': '16'
    },
    'nn': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'nn'),
        'binary': 'run',
        'verify': 'verify',
        'args': os.path.join(DIR_APPS, 'rodinia', 'data', 'nn', 'list640k_64.txt')
    },
    'heartwall': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'heartwall'),
        'binary': 'run',
        'verify': 'verify',
        'args': '{} 2'.format(os.path.join(DIR_APPS, 'rodinia', 'data', 'heartwall', 'test.avi'))
    },
    'bfs': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'bfs'),
        'binary': 'run',
        'verify': 'verify',
        'args': ''
    },
    'hotspot': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'hotspot'),
        'binary': 'run',
        'verify': 'verify',
        'args': ''
    },
    'pathfinder': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'pathfinder'),
        'binary': 'run',
        'verify': 'verify',
        'args': ''
    },
    'b+tree': {
        'dir': os.path.join(DIR_APPS, 'rodinia', 'cuda', 'b+tree'),
        'binary': 'run',
        'verify': 'verify',
        'args': ''
    }
}
