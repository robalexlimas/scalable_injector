import os


APPS = [
    'backprop',
    'gaussian',
    'nn',
    'lavamd',
    'lu',
    'heartwall',
    'cfd'
]

# DEBUG = str(os.getenv('DEBUG')).startswith('1')
BASE_DIR = os.getcwd()
DIR_INJECTOR = os.path.join(os.getcwd(), '..')
DEBUG = True
LOG_PATH = os.path.join(BASE_DIR, 'log.txt')
