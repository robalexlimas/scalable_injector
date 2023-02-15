import os


BASE_DIR = os.getcwd()

APPS = [
    'backprop',
    'gaussian',
    'nn',
    'lavamd',
    'lud',
    'heartwall'
]

GPUS = {
    'SM75_RTX2060': {
        'SM': 30,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM7_TITANV': {
        'SM': 80,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX': {
        'SM': 28,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN': {
        'SM': 14,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }
}
