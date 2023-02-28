from math import log2


def save_csv(fault_list, filename):
    with open(filename, 'w+') as file:
        file.writelines(fault_list)


def convert_mask(mask):
    return log2(int(mask))
