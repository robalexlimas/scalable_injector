from common import APPS, GPUS

import random


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
                                    for mask in range(32):
                                        for bit in [0, 1]:
                                            fault = '1,1,{},{},{},{},{},{},{},{},{},{}\n'.format(
                                                app,
                                                sm,
                                                sub_core,
                                                core_type,
                                                core_id,
                                                in_out,
                                                operand,
                                                2 ** mask,
                                                bit,
                                                gpu
                                            )
                                            fault_list.append(fault)
    return fault_list


def random_list(faults_list, n):
    fault_list = random.sample(faults_list, n)
    return fault_list


def save_csv(fault_list, filename):
    with open(filename, 'w') as file:
        file.writelines(fault_list)


if __name__ == '__main__':
    exhaustive = exhaustive_fault_list()
    print(len(exhaustive))
    random = random_list(exhaustive, 100)
    save_csv(exhaustive, 'exhaustive.csv')
    save_csv(random, 'random.csv')
