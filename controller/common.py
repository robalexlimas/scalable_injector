import os


BASE_DIR = os.getcwd()

HPC_DIR = '/home/rlimassierra/FaultCampaings/apps'

CORE_TYPE = {
    '2': 'special unit',
    '3': 'tensor core',
    '5': 'floating-point',
    '6': 'integer'
}

APPS = [
    'backprop',
    'gaussian',
    'nn',
    'heartwall',
    'bfs',
    'hotspot',
    'pathfinder',
    'b+tree'
]

TIMEOUTS = {
    'backprop': {
        'SM75_RTX2060': 0,
        'SM7_TITANV': 1,
        'SM6_TITANX': 2,
        'SM3_KEPLER_TITAN': 3
    },
    'gaussian': {
        'SM75_RTX2060': 0,
        'SM7_TITANV': 0,
        'SM6_TITANX': 0,
        'SM3_KEPLER_TITAN': 0
    },
    'nn': {
        'SM75_RTX2060': 0,
        'SM7_TITANV': 0,
        'SM6_TITANX': 0,
        'SM3_KEPLER_TITAN': 0
    },
    'heartwall': {
        'SM75_RTX2060': 0,
        'SM7_TITANV': 0,
        'SM6_TITANX': 0,
        'SM3_KEPLER_TITAN': 0
    },
    'bfs': {
        'SM75_RTX2060': 0,
        'SM7_TITANV': 0,
        'SM6_TITANX': 0,
        'SM3_KEPLER_TITAN': 0
    },
    'hotspot': {
        'SM75_RTX2060': 0,
        'SM7_TITANV': 0,
        'SM6_TITANX': 0,
        'SM3_KEPLER_TITAN': 0
    },
    'pathfinder': {
        'SM75_RTX2060': 0,
        'SM7_TITANV': 0,
        'SM6_TITANX': 0,
        'SM3_KEPLER_TITAN': 0
    },
    'b+tree': {
        'SM75_RTX2060': 0,
        'SM7_TITANV': 0,
        'SM6_TITANX': 0,
        'SM3_KEPLER_TITAN': 0
    }
}

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
