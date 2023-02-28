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
    'SM75_RTX2060_2SM': {
        'SM': 2,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM75_RTX2060_4SM': {
        'SM': 4,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM75_RTX2060_8SM': {
        'SM': 8,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM75_RTX2060_16SM': {
        'SM': 16,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM75_RTX2060_32SM': {
        'SM': 32,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM75_RTX2060_64SM': {
        'SM': 64,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM75_RTX2060_1SUBSM': {
        'SM': 30,
        'SM_SUB_CORE': 1,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM75_RTX2060_8SUBSM': {
        'SM': 30,
        'SM_SUB_CORE': 8,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM75_RTX2060_12SUBSM': {
        'SM': 30,
        'SM_SUB_CORE': 12,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }, 
    'SM75_RTX2060_16SUBSM': {
        'SM': 30,
        'SM_SUB_CORE': 16,
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
    'SM7_TITANV_2SM': {
        'SM': 2,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM7_TITANV_4SM': {
        'SM': 4,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM7_TITANV_8SM': {
        'SM': 8,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM7_TITANV_16SM': {
        'SM': 16,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM7_TITANV_32SM': {
        'SM': 32,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM7_TITANV_64SM': {
        'SM': 64,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM7_TITANV_1SUBSM': {
        'SM': 80,
        'SM_SUB_CORE': 1,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM7_TITANV_8SUBSM': {
        'SM': 80,
        'SM_SUB_CORE': 8,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM7_TITANV_12SUBSM': {
        'SM': 80,
        'SM_SUB_CORE': 12,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM7_TITANV_16SUBSM': {
        'SM': 80,
        'SM_SUB_CORE': 16,
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
    'SM6_TITANX_2SM': {
        'SM': 2,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX_4SM': {
        'SM': 4,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX_8SM': {
        'SM': 8,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX_16SM': {
        'SM': 16,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX_32SM': {
        'SM': 32,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX_64SM': {
        'SM': 64,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX_1SUBSM': {
        'SM': 28,
        'SM_SUB_CORE': 1,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX_8SUBSM': {
        'SM': 28,
        'SM_SUB_CORE': 8,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX_12SUBSM': {
        'SM': 28,
        'SM_SUB_CORE': 12,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM6_TITANX_16SUBSM': {
        'SM': 28,
        'SM_SUB_CORE': 16,
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
    },
    'SM3_KEPLER_TITAN_2SM': {
        'SM': 2,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN_4SM': {
        'SM': 4,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN_8SM': {
        'SM': 8,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN_16SM': {
        'SM': 16,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN_32SM': {
        'SM': 32,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN_64SM': {
        'SM': 64,
        'SM_SUB_CORE': 4,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN_1SUBSM': {
        'SM': 14,
        'SM_SUB_CORE': 1,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN_8SUBSM': {
        'SM': 14,
        'SM_SUB_CORE': 8,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN_12SUBSM': {
        'SM': 14,
        'SM_SUB_CORE': 12,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    },
    'SM3_KEPLER_TITAN_16SUBSM': {
        'SM': 14,
        'SM_SUB_CORE': 16,
        'CORE_TYPE': [2, 5, 6],
        'CORE_ID': 16,
        'IN_OUT': [0, 1],
        'OPERAND': [0, 1, 2]
    }
}
