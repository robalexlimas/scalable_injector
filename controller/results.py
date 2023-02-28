import os


from math import log2


from common import BASE_DIR



HPC_DIR = '/home/rlimassierra/FaultCampaings/apps'

CORE_TYPE = {
    '2': 'special unit',
    '3': 'tensor core',
    '5': 'floating-point',
    '6': 'integer'
}


def convert_mask(mask):
    return log2(int(mask))


def save_csv(results):
    result_dir = os.path.join(BASE_DIR, 'results.csv')
    with open(result_dir, 'w') as file:
        file.writelines(results)


def read_results():
    results = ['debug,enable,app,sm,sm_sub_core,core_type,core_id,in_out,operand,mask,stuckat,cycles,gpu,masked,sdc,due\n']
    apps = os.listdir(HPC_DIR)
    for app in apps:
        app_dir = os.path.join(HPC_DIR, app)
        gpus = os.listdir(app_dir)
        for gpu in gpus:
            gpu_dir = os.path.join(app_dir, gpu)
            logs_dir = os.path.join(gpu_dir, 'logs')
            logs = os.listdir(logs_dir)
            for log in logs:
                # debug enable app sm sm_sub_core core_type core_id in_out operand mask stuckat cycles gpu
                fault = log.split('.')[0].split(',')
                fault[5] = CORE_TYPE[fault[5]]
                fault[9] = convert_mask(fault[9])
                fault_str = ','.join(fault)
                log_dir = os.path.join(logs_dir, log)
                with open(log_dir, 'r') as log_file:
                    lines = log_file.readlines()
                    if 'INFO: MASKED' in lines:
                        results.append('{},1,0,0\n'.format(fault_str))
                    if 'WARNING: SDC' in lines:
                        results.append('{},0,1,0\n'.format(fault_str))
                    if 'ERROR: DUE' in lines:
                        results.append('{},0,0,1\n'.format(fault_str))
    save_csv(results)


if __name__ == '__main__':
    read_results()
