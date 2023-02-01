from common import DIR_GPGPUSIM_CONFIG


import os, shutil


def load_params(app_script, fault):
    files = os.listdir(DIR_GPGPUSIM_CONFIG)
    for file in files:
        source_file = os.path.join(DIR_GPGPUSIM_CONFIG, file)
        destination_file = os.path.join(app_script, file)
        shutil.copy(source_file, destination_file)
