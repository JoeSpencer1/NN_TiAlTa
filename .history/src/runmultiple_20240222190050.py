import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([  
        "validation_one('sigma_y', 'TI33_Berkovich_rough', 'TI33_Berkovich', 1)",
        "validation_one('Estar', 'TI33_Berkovich_rough', 'TI33_Berkovich', 1)",
        "validation_one('sigma_y', 'TI33_Berkovich_rough', 'TI33_Berkovich', 2)",
        "validation_one('Estar', 'TI33_Berkovich_rough', 'TI33_Berkovich', 2)",
        "validation_one('sigma_y', 'TI33_Berkovich_rough', 'TI33_Berkovich', 3)",
        "validation_one('Estar', 'TI33_Berkovich_rough', 'TI33_Berkovich', 3)",
        "validation_one('sigma_y', 'TI33_Berkovich_rough', 'TI33_Berkovich', 4)",
        "validation_one('Estar', 'TI33_Berkovich_rough', 'TI33_Berkovich', 4)",
        "validation_one('sigma_y', 'TI33_Berkovich_rough', 'TI33_Berkovich', 5)",
        "validation_one('Estar', 'TI33_Berkovich_rough', 'TI33_Berkovich', 5)",
        "validation_one('sigma_y', 'TI33_Berkovich_rough', 'TI33_Berkovich', 6)",
        "validation_one('Estar', 'TI33_Berkovich_rough', 'TI33_Berkovich', 6)",
        "validation_one('sigma_y', 'TI33_Berkovich_rough', 'TI33_Berkovich', 8)",
        "validation_one('Estar', 'TI33_Berkovich_rough', 'TI33_Berkovich', 8)",
        "validation_one('sigma_y', 'TI33_Berkovich_rough', 'TI33_Berkovich', 10)",
        "validation_one('Estar', 'TI33_Berkovich_rough', 'TI33_Berkovich', 10)",
        "validation_one('sigma_y', 'TI33_Berkovich_rough', 'TI33_Berkovich', 20)",
        "validation_one('Estar', 'TI33_Berkovich_rough', 'TI33_Berkovich', 20)"
        ])
    
    processes = []
    num_processes = len(arguments)
    for i in range(num_processes):        
        process = multiprocessing.Process(target=run_main, args=(arguments[i],))
        processes.append(process)

    for process in processes:
        process.start()
    for process in processes:
        process.join()
        
        

        '''
        (All 3 data types)
        "validation_exp_cross2('sigma_y', 0, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 0, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('sigma_y', 1, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 1, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('sigma_y', 2, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 2, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('sigma_y', 3, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 3, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('sigma_y', 4, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 4, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('sigma_y', 5, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 5, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('sigma_y', 6, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 6, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('sigma_y', 8, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 8, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('sigma_y', 10, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 10, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('sigma_y', 20, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_exp_cross2('Estar', 20, 'TI33_conical_70.3', 'TI33_Berkovich', 'TI33_25', 'TI33_25')"   
        
        (2 data types)
        "validation_mf('sigma_y', 0, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 0, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 1, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 1, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 2, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 2, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 3, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 3, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 4, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 4, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 5, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 5, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 6, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 6, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 8, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 8, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 10, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 10, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 20, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 20, 'TI33_Berkovich', 'TI33_25', 'TI33_25')"
        
        (1 data type)  
        "validation_one('sigma_y', 'TI33_conical_70.3', 'TI33_conical_70.3', 1)",
        "validation_one('Estar', 'TI33_conical_70.3', 'TI33_conical_70.3', 1)",
        "validation_one('sigma_y', 'TI33_conical_70.3', 'TI33_conical_70.3', 2)",
        "validation_one('Estar', 'TI33_conical_70.3', 'TI33_conical_70.3', 2)",
        "validation_one('sigma_y', 'TI33_conical_70.3', 'TI33_conical_70.3', 3)",
        "validation_one('Estar', 'TI33_conical_70.3', 'TI33_conical_70.3', 3)",
        "validation_one('sigma_y', 'TI33_conical_70.3', 'TI33_conical_70.3', 4)",
        "validation_one('Estar', 'TI33_conical_70.3', 'TI33_conical_70.3', 4)",
        "validation_one('sigma_y', 'TI33_conical_70.3', 'TI33_conical_70.3', 5)",
        "validation_one('Estar', 'TI33_conical_70.3', 'TI33_conical_70.3', 5)",
        "validation_one('sigma_y', 'TI33_conical_70.3', 'TI33_conical_70.3', 6)",
        "validation_one('Estar', 'TI33_conical_70.3', 'TI33_conical_70.3', 6)",
        "validation_one('sigma_y', 'TI33_conical_70.3', 'TI33_conical_70.3', 8)",
        "validation_one('Estar', 'TI33_conical_70.3', 'TI33_conical_70.3', 8)",
        "validation_one('sigma_y', 'TI33_conical_70.3', 'TI33_conical_70.3', 10)",
        "validation_one('Estar', 'TI33_conical_70.3', 'TI33_conical_70.3', 10)",
        "validation_one('sigma_y', 'TI33_conical_70.3', 'TI33_conical_70.3', 20)",
        "validation_one('Estar', 'TI33_conical_70.3', 'TI33_conical_70.3', 20)"
        
        '''