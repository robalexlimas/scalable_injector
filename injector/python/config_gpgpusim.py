from common import DIR_GPGPUSIM_CONFIG


from string import Template
import os, shutil


def load_params(app_script, fault):
    config_dir = os.path.join(DIR_GPGPUSIM_CONFIG, fault['gpu'])
    files = os.listdir(config_dir)
    for file in files:
        source_file = os.path.join(config_dir, file)
        destination_file = os.path.join(app_script, file)
        shutil.copy(source_file, destination_file)
    config_file = os.path.join(app_script, 'gpgpusim.config')
    injector_params = """
# fault injector
-fault_debug $debug
-fault_enable $enable
-fault_sm_id $sm_id
-fault_sm_sub_core_id $sm_sub_core
-fault_core_type $core_type
-fault_core_id $core_id
-fault_in_out $in_out
-fault_operand $operand
-fault_mask $mask
-fault_stuckat $stuckat
-fault_timeout_cycles $cycles
    """
    params = Template(injector_params).substitute(
        debug=fault['debug'],
        enable=fault['enable'],
        sm_id=fault['sm_id'],
        sm_sub_core=fault['sm_sub_core_id'],
        core_type=fault['core_type'],
        core_id=fault['core_id'],
        in_out=fault['in_out'],
        operand=fault['operand'],
        mask=fault['mask'],
        stuckat=fault['stuckat'],
        cycles=fault['cycles']
    )
    with open(config_file, 'a') as file:
        file.write(params)
