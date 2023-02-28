import os


from common import BASE_DIR, CORE_TYPE, HPC_DIR
from utils import convert_mask, save_csv


def compare_faults(reference, value):
    faults = ['{}\n'.format(','.join(fault.split(',')[:-3])) for fault in value]
    reference.extend(faults)
    return list(set(reference))


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
                fault = log.split('.')[0]
                fault_array = fault.split(',')
                fault_array[5] = CORE_TYPE[fault_array[5]]
                fault_array[9] = convert_mask(fault_array[9])
                fault_str = ','.join(fault_array)
                log_dir = os.path.join(logs_dir, log)
                with open(log_dir, 'r') as log_file:
                    lines = log_file.readlines()
                    if 'INFO: MASKED' in lines:
                        results.append('{},1,0,0\n'.format(fault_str))
                    elif 'WARNING: SDC' in lines:
                        results.append('{},0,1,0\n'.format(fault_str))
                    elif 'ERROR: DUE' in lines:
                        results.append('{},0,0,1\n'.format(fault_str))
    return results


if __name__ == '__main__':
    results = read_results()
    result_dir = os.path.join(BASE_DIR, 'results.csv')
    save_csv(results, result_dir)
    random_faults_dir = os.path.join(BASE_DIR, 'random.csv')
    random_file = open(random_faults_dir, 'r')
    random_faults = random_file.readlines()
    random_file.close()
    missing = compare_faults(random_faults, results)
    missing_dir = os.path.join(BASE_DIR, 'missing.csv')
    save_csv(missing, missing_dir)
