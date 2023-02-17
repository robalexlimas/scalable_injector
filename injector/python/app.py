from common import APPS, DIR_INJECTOR, DIR_RESULTS
from execute import execute_golden_app, execute_app_with_fault
from log import log


import argparse, json, logging, os, tarfile, time


logging.basicConfig(level=logging.DEBUG)


def get_args():
    parser = argparse.ArgumentParser(description='Fault injector build on the top of GPGPU-Sim.')
    parser.add_argument('debug', type=int)
    parser.add_argument('enable', type=int)
    parser.add_argument('app_name', type=str)
    parser.add_argument('sm_id', type=int)
    parser.add_argument('sm_sub_core_id', type=int)
    parser.add_argument('core_type', type=int)
    parser.add_argument('core_id', type=int)
    parser.add_argument('in_out', type=int)
    parser.add_argument('operand', type=int)
    parser.add_argument('mask', type=int)
    parser.add_argument('stuckat', type=int)
    parser.add_argument('gpu', type=str)
    args = parser.parse_args()
    return vars(args)


def make_tar_file(fault):
    results = os.listdir(DIR_RESULTS)
    tar_name = '{}_{}_{}_{}_{}_{}_{}_{}.tar.gz'.format(
        fault['sm_id'],
        fault['sm_sub_core_id'],
        fault['core_type'],
        fault['core_id'],
        fault['in_out'],
        fault['operand'],
        fault['mask'],
        fault['stuckat']
    )
    tar_dir = os.path.join(DIR_RESULTS, tar_name)
    logging.info('Saving files in {}'.format(tar_dir))
    tar = tarfile.open(tar_dir, 'w:gz')
    for file in results:
        logging.info('File: {}'.format(file))
        file_dir = os.path.join(DIR_RESULTS, file)
        tar.add(file_dir, file)
    tar.close()
    logging.info('Delete files')
    for file in results:
        file_dir = os.path.join(DIR_RESULTS, file)
        if not file_dir.endswith('tar.gz'):
            os.remove(file_dir)


if __name__ == '__main__':
    args = get_args()
    logging.info('Execute app {} on {} GPU'.format(args['app_name'], args['gpu']))
    if args['enable']:
        execute_app_with_fault(args['app_name'], args)
    else:
        execute_golden_app(args['app_name'], args)
    make_tar_file(args)
    logging.info('End simulation')
