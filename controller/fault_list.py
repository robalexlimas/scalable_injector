from random import choice, randint


from common import APPS, GPUS, TIMEOUTS
from utils import save_csv


def exhaustive_fault_list():
    fault_list = []
    for app in APPS:
        for gpu in GPUS:
            arch = GPUS[gpu]
            for sm in range(arch['SM']):
                for sub_core in range(arch['SM_SUB_CORE']):
                    for core_type in arch['CORE_TYPE']:
                        for core_id in range(arch['CORE_ID']):
                            for in_out in arch['IN_OUT']:
                                for operand in arch['OPERAND']:
                                    if in_out == 1 and operand == 1:
                                        for mask in range(32):
                                            for bit in [0, 1]:
                                                fault = '1,1,{},{},{},{},{},{},{},{},{},{},{}\n'.format(
                                                    app,
                                                    0,
                                                    sub_core,
                                                    core_type,
                                                    core_id,
                                                    in_out,
                                                    operand,
                                                    2 ** mask,
                                                    bit,
                                                    TIMEOUTS[app][gpu],
                                                    gpu
                                                )
                                                fault_list.append(fault)
                                            fault_list.append(fault)
    return fault_list


def random_list(n):
    fault_list = []
    for app in APPS:
        for gpu in GPUS:
            arch = GPUS[gpu]
            for in_out in arch['IN_OUT']:
                for core_type in arch['CORE_TYPE']:
                    counter = 0
                    while True:
                        sm = 0
                        sub_core = randint(0, arch['SM_SUB_CORE']-1)
                        core_id = randint(0, arch['CORE_ID']-1)
                        if in_out == 1 or core_type == 2:
                            operand = 0
                        else:
                            operand = choice(arch['OPERAND'])
                        mask = randint(0, 31)
                        st = randint(0, 1)
                        cycles = TIMEOUTS[app][gpu]
                        fault = '1,1,{},{},{},{},{},{},{},{},{},{},{}\n'.format(
                            app,
                            sm,
                            sub_core,
                            core_type,
                            core_id,
                            in_out,
                            operand,
                            2 ** mask,
                            st,
                            cycles,
                            gpu
                        )
                        if not fault in fault_list and counter < n:
                            fault_list.append(fault)
                            counter += 1
                        if counter == n:
                            save_faults(fault_list, 12, '{}_{}_*.csv'.format(app, gpu))
                            fault_list = []
                            break
    return fault_list


def save_faults(faults, total, filename):
    aux_ = []
    aux = []
    count = 0
    for fault in faults:
        aux_.append(fault)
        if count == total - 1:
            count = 0
            aux.append(aux_)
            aux_ = []
        else:
            count += 1
    for i, part in enumerate(aux):
        filename_ = filename.replace('*', str(i))
        save_csv(part, 'faults/' + filename_)


def golden_apps_list():
    for app in APPS:
        golden_list = []
        for gpu in GPUS:
            golden = '0,0,{},0,0,0,0,0,0,0,0,0,{}\n'.format(
                app,
                gpu
            )
            golden_list.append(golden)
        index_file = 0
        index = 0
        for golden in golden_list:
            if index < 12:
                with open('{}_golden_{}.csv'.format(app, index_file), 'a+') as file:
                    file.write(golden)
                    index += 1
            else:
                index_file += 1
                index = 0
                with open('{}_golden_{}.csv'.format(app, index_file), 'a+') as file:
                    file.write(golden)


if __name__ == '__main__':
    #golden_apps_list()
    # exhaustive = exhaustive_fault_list()
    # save_csv(exhaustive, 'exhaustive.csv')
    random = random_list(504)
    # save_csv(random, 'random.csv')
