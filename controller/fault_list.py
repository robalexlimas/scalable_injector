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
            counter = 0
            while True:
                sm = 0
                sub_core = randint(0, arch['SM_SUB_CORE']-1)
                core_type = choice(arch['CORE_TYPE'])
                core_id = randint(0, arch['CORE_ID']-1)
                in_out = choice(arch['IN_OUT'])
                operand = choice(arch['OPERAND'])
                mask = randint(0, 31)
                bit = randint(0, 1)
                if in_out == 1 and operand == 0:
                    fault = '1,1,{},{},{},{},{},{},{},{},{},{},{}\n'.format(
                        app,
                        sm,
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
                    if not fault in fault_list and counter < n:
                        fault_list.append(fault)
                        counter += 1
                    if counter == n:
                        break
    return fault_list


def golden_apps_list():
    golden_list = []
    for app in APPS:
        for gpu in GPUS:
            golden = '0,0,{},0,0,0,0,0,0,0,0,0,{}\n'.format(
                app,
                gpu
            )
            golden_list.append(golden)
    save_csv(golden_list, 'golden.csv')


if __name__ == '__main__':
    golden_apps_list()
    # exhaustive = exhaustive_fault_list()
    # save_csv(exhaustive, 'exhaustive.csv')
    random = random_list(100)
    save_csv(random, 'random.csv')
