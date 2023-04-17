import os, tarfile, shutil


from common import BASE_DIR, CORE_TYPE, HPC_DIR
from utils import convert_mask, save_csv


def compare_faults(reference, value):
    faults = ['{}\n'.format(','.join(fault.split(',')[:-4])) for fault in value]
    faults = list(filter(lambda fault: fault.endswith('1\n'), faults))
    reference.extend(faults)
    return list(set(reference))


def read_results():
    results_list = ['debug,enable,app,sm,sm_sub_core,core_type,core_id,in_out,operand,mask,stuckat,cycles,gpu,masked,sdc,due,error\n']
    apps = os.listdir(HPC_DIR)
    for app in apps:
        print(app)
        app_dir = os.path.join(HPC_DIR, app)
        gpus = os.listdir(app_dir)
        gpus = list(filter(lambda folder: folder != 'logs' and folder != 'sbatch', gpus))
        for gpu in gpus:
            gpu_dir = os.path.join(app_dir, gpu)
            results_dir = os.path.join(gpu_dir, 'results')
            total_files = os.listdir(results_dir)
            results = list(filter(lambda file: file.endswith('.tar.gz'), total_files))
            for result in results:
                os.mkdir('extracted')
                # debug enable app sm sm_sub_core core_type core_id in_out operand mask stuckat cycles gpu
                fault = '0_0_{}_{}_{}'.format(
                    app.split('_')[0],
                    result.split('.')[0],
                    '0'
                )
                fault_array = fault.split('_')
                fault_array[5] = CORE_TYPE[fault_array[5]]
                fault_array[9] = str(convert_mask(fault_array[9]))
                fault_str = ','.join(fault_array)
                fault_str = '{},{}'.format(fault_str, gpu)
                result_dir = os.path.join(results_dir, result)
                # Tar file
                tar_file = tarfile.open(result_dir)
                tar_file.extractall(os.path.join(BASE_DIR, 'extracted'))
                tar_file.close()
                files_names = os.listdir(os.path.join(BASE_DIR, 'extracted'))
                app_name = ''.join(app.split('_')[:-2])
                log_dir = os.path.join(BASE_DIR, 'extracted', '{}_golden.log'.format(app_name))
                err_dir = os.path.join(BASE_DIR, 'extracted', 'stderr.log')
                with open(err_dir, 'r') as err_file:
                    lines = err_file.readlines()
                    if len(lines) > 0:
                        error = '1'
                    else:
                        error = '0'
                with open(log_dir, 'r') as log_file:
                    lines = log_file.readlines()
                    if 'INFO: MASKED\n' in lines:
                        results_list.append('{},1,0,0,{}\n'.format(fault_str, error))
                    elif 'WARNING: SDC\n' in lines:
                        results_list.append('{},0,1,0,{}\n'.format(fault_str, error))
                    elif 'ERROR: DUE\n' in lines:
                        results_list.append('{},0,0,1,{}\n'.format(fault_str, error))
                shutil.rmtree('extracted')
    return results_list


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
