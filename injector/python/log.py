import datetime

from common import LOG_PATH


def log(message):
    now = datetime.datetime.now().strftime('%Y_%m_%d %H:%M')
    with open(LOG_PATH, mode='a') as f:
        f.write('******************************************************************************************************'
                '*****************\n')
        f.write('{}\n'.format(now))
        f.write('{}\n'.format(message))
        f.write('******************************************************************************************************'
                '*****************\n')
