import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([    
        "validation_one('sigma_y', 'TI33_25', 'TI33_25', 1)",
        "validation_one('Estar', 'TI33_25', 'TI33_25', 1)",
        "validation_one('sigma_y', 'TI33_25', 'TI33_25', 2)",
        "validation_one('Estar', 'TI33_25', 'TI33_25', 2)",
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
        

        "validation_exp_cross2('sigma_y', 2, 'B30901', 'B30901')",
        "validation_exp_cross2('Estar', 2, 'B30901', 'B30901')",
        "validation_exp_cross2('sigma_y', 3, 'B30901', 'B30901')",
        "validation_exp_cross2('Estar', 3, 'B30901', 'B30901')",
        "validation_exp_cross2('sigma_y', 4, 'B30901', 'B30901')",
        "validation_exp_cross2('Estar', 4, 'B30901', 'B30901')",
        "validation_exp_cross2('sigma_y', 5, 'B30901', 'B30901')",
        "validation_exp_cross2('Estar', 5, 'B30901', 'B30901')",
        "validation_exp_cross2('sigma_y', 6, 'B30901', 'B30901')",
        "validation_exp_cross2('Estar', 6, 'B30901', 'B30901')",
        "validation_exp_cross2('sigma_y', 8, 'B30901', 'B30901')",
        "validation_exp_cross2('Estar', 8, 'B30901', 'B30901')",
        "validation_exp_cross2('sigma_y', 10, 'B30901', 'B30901')",
        "validation_exp_cross2('Estar', 10, 'B30901', 'B30901')",


        "validation_mf('sigma_y', 3, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 3, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 6, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 6, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 9, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 9, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 12, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 12, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 15, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 15, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 18, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 18, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 21, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 21, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 24, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 24, 'TI33_Berkovich', 'TI33_25', 'TI33_25')"


        "validation_mf('sigma_y', 3, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 3, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 6, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 6, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 9, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 9, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 12, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 12, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 15, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 15, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 18, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 18, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 21, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 21, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('sigma_y', 24, 'TI33_Berkovich', 'TI33_25', 'TI33_25')",
        "validation_mf('Estar', 24, 'TI33_Berkovich', 'TI33_25', 'TI33_25')"


        "validation_exp_cross2('Estar', 2, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('Estar', 3, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('Estar', 4, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('Estar', 5, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('Estar', 8, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('Estar', 10, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",

        "validation_exp_cross2('sigma_y', 2, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('sigma_y', 3, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('sigma_y', 4, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('sigma_y', 5, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('sigma_y', 8, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",
        "validation_exp_cross2('sigma_y', 10, 'Berkovich', 'FEM_70deg', 'B3090', 'B3090')",

        "validation_FEM('sigma_y', 'TI33_25', 'TI33_25',3)",
        "validation_FEM('sigma_y', 'TI33_25', 'TI33_25',6)",
        "validation_FEM('sigma_y', 'TI33_25', 'TI33_25',9)",
        "validation_FEM('sigma_y', 'TI33_25', 'TI33_25',12)",
        "validation_FEM('sigma_y', 'TI33_25', 'TI33_25',15)",
        "validation_FEM('sigma_y', 'TI33_25', 'TI33_25',18)",
        "validation_FEM('sigma_y', 'TI33_25', 'TI33_25',21)",
        "validation_FEM('Estar', 'TI33_25', 'TI33_25', 3)",
        "validation_FEM('Estar', 'TI33_25', 'TI33_25', 6)",
        "validation_FEM('Estar', 'TI33_25', 'TI33_25', 9)",
        "validation_FEM('Estar', 'TI33_25', 'TI33_25', 12)",
        "validation_FEM('Estar', 'TI33_25', 'TI33_25', 15)",
        "validation_FEM('Estar', 'TI33_25', 'TI33_25', 18)",
        "validation_FEM('Estar', 'TI33_25', 'TI33_25', 21)"


        "validation_mf('sigma_y', 10, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('Estar', 10, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('sigma_y', 20, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('Estar', 20, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('sigma_y', 40, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('Estar', 40, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('sigma_y', 50, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('Estar', 50, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('sigma_y', 60, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('Estar', 60, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('sigma_y', 70, 'FEM_70deg', 'B3090', 'B3090')",
        "validation_mf('Estar', 70, 'FEM_70deg', 'B3090', 'B3090')"


        
        "validation_FEM('sigma_y', 'TI33_Berkovich', 'TI33_25',4)",
        "validation_FEM('sigma_y', 'TI33_Berkovich', 'TI33_25',6)",
        "validation_FEM('sigma_y', 'TI33_Berkovich', 'TI33_25',8)",
        "validation_FEM('sigma_y', 'TI33_Berkovich', 'TI33_25',10)",
        "validation_FEM('sigma_y', 'TI33_Berkovich', 'TI33_25',12)",
        "validation_FEM('sigma_y', 'TI33_Berkovich', 'TI33_25',14)",
        "validation_FEM('sigma_y', 'TI33_Berkovich', 'TI33_25',16)",
        "validation_FEM('Estar', 'TI33_Berkovich', 'TI33_25', 2)",
        "validation_FEM('Estar', 'TI33_Berkovich', 'TI33_25', 4)",
        "validation_FEM('Estar', 'TI33_Berkovich', 'TI33_25', 6)",
        "validation_FEM('Estar', 'TI33_Berkovich', 'TI33_25', 8)",
        "validation_FEM('Estar', 'TI33_Berkovich', 'TI33_25', 10)",
        "validation_FEM('Estar', 'TI33_Berkovich', 'TI33_25', 12)",
        "validation_FEM('Estar', 'TI33_Berkovich', 'TI33_25', 14)",
        
        "validation_FEM('sigma_y', 'FEM_70deg', 'FEM_70deg', 10)",
        "validation_FEM('sigma_y', 'FEM_70deg', 'FEM_70deg', 70)",
        "validation_FEM('Estar', 'FEM_70deg', 'FEM_70deg', 10)",
        "validation_FEM('Estar', 'FEM_70deg', 'FEM_70deg', 70)",
        "validation_FEM('sigma_y', 'TI33_Berkovich_rough', 'TI33_25',4)",
        "validation_FEM('sigma_y', 'TI33_Berkovich_rough', 'TI33_25',6)",
        "validation_FEM('sigma_y', 'TI33_Berkovich_rough', 'TI33_25',8)",
        "validation_FEM('sigma_y', 'TI33_Berkovich_rough', 'TI33_25',10)",
        "validation_FEM('sigma_y', 'TI33_Berkovich_rough', 'TI33_25',12)",
        "validation_FEM('sigma_y', 'TI33_Berkovich_rough', 'TI33_25',14)",
        "validation_FEM('sigma_y', 'TI33_Berkovich_rough', 'TI33_25',16)",
        "validation_FEM('Estar', 'TI33_Berkovich_rough', 'TI33_25', 2)",
        "validation_FEM('Estar', 'TI33_Berkovich_rough', 'TI33_25', 4)",
        "validation_FEM('Estar', 'TI33_Berkovich_rough', 'TI33_25', 6)",
        "validation_FEM('Estar', 'TI33_Berkovich_rough', 'TI33_25', 8)",
        "validation_FEM('Estar', 'TI33_Berkovich_rough', 'TI33_25', 10)",
        "validation_FEM('Estar', 'TI33_Berkovich_rough', 'TI33_25', 12)",
        "validation_FEM('Estar', 'TI33_Berkovich_rough', 'TI33_25', 14)",
        "validation_FEM('Estar', 'TI33_Berkovich_rough', 'TI33_25', 16)"
        
        "validation_FEM('sigma_y', 'FEM_70deg', 'FEM_70deg', 20)",
        "validation_FEM('sigma_y', 'FEM_70deg', 'FEM_70deg', 30)",
        "validation_FEM('sigma_y', 'FEM_70deg', 'FEM_70deg', 40)",
        "validation_FEM('sigma_y', 'FEM_70deg', 'FEM_70deg', 50)",
        "validation_FEM('sigma_y', 'FEM_70deg', 'FEM_70deg', 60)",
        "validation_FEM('sigma_y', 'FEM_70deg', 'FEM_70deg', 70)",
        "validation_FEM('Estar', 'FEM_70deg', 'FEM_70deg', 20)",
        "validation_FEM('Estar', 'FEM_70deg', 'FEM_70deg', 30)",
        "validation_FEM('Estar', 'FEM_70deg', 'FEM_70deg', 40)",
        "validation_FEM('Estar', 'FEM_70deg', 'FEM_70deg', 50)",
        "validation_FEM('Estar', 'FEM_70deg', 'FEM_70deg', 60)",
        "validation_FEM('Estar', 'FEM_70deg', 'FEM_70deg', 70)",
        
        ,
        "validation_FEM('Estar', 'FEM_70deg', 10)"


        "validation_three('Estar', 0, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('Estar', 1, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('Estar', 1, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('Estar', 3, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('Estar', 4, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('Estar', 5, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('Estar', 6, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('Estar', 8, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('Estar', 10, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('Estar', 20, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 0, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 1, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 1, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 3, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 4, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 5, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 6, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 8, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 10, 'TI33_25', 'TI33_25', lay=2)",
        "validation_three('sigma_y', 20, 'TI33_25', 'TI33_25', lay=2)"
        
        '''
        '''
        "validation_two('Estar', 5, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('Estar', 10, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('Estar', 20, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('sigma_y', 0, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('sigma_y', 5, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('sigma_y', 10, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('sigma_y', 20, 'TI33_25', 'FEM', 'Berk', lay=2)",
        '''
        '''
        "validation_three('Estar', 0, 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 5, 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 10, 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 20, 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 0, 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 5, 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 10, 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 20, 'TI33_25', 'TI33_25')"
        '''
        '''
        "validation_two('Estar', 0, 'TI33_25', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 1, 'TI33_25', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 20, 'TI33_25', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 0, 'TI33_25', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 1, 'TI33_25', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 20, 'TI33_25', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 0, 'TI33_25', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 1, 'TI33_25', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 20, 'TI33_25', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 0, 'TI33_25', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 1, 'TI33_25', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 20, 'TI33_25', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 0, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('Estar', 1, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('Estar', 20, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('sigma_y', 0, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('sigma_y', 1, 'TI33_25', 'FEM', 'Berk', lay=2)",
        "validation_two('sigma_y', 20, 'TI33_25', 'FEM', 'Berk', lay=2)",
        '''
        '''
        "validation_two('Estar', 1, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 2, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 3, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 4, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 5, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 6, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 8, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 10, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('Estar', 20, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 1, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 2, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 3, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 4, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 5, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 6, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 8, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 10, 'Al6061', 'FEM', 'Exp', lay=2)",
        "validation_two('sigma_y', 20, 'Al6061', 'FEM', 'Exp', lay=2)",
        '''
        '''
        "validation_two('Estar', 1, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 2, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 3, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 4, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 5, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 6, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 8, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 10, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('Estar', 20, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 1, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 2, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 3, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 4, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 5, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 6, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 8, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 10, 'Al6061', 'Berk', 'Exp', lay=2)",
        "validation_two('sigma_y', 20, 'Al6061', 'Berk', 'Exp', lay=2)"
        '''
        '''
        "validation_one('Estar', ['TI33_25'], 'TI33_25', 'Exp', [1])",
        "validation_one('Estar', ['TI33_25'], 'TI33_25', 'Exp', [2])",
        "validation_one('Estar', ['TI33_25'], 'TI33_25', 'Exp', [3])",
        "validation_one('Estar', ['TI33_25'], 'TI33_25', 'Exp', [4])",
        "validation_one('Estar', ['TI33_25'], 'TI33_25', 'Exp', [5])",
        "validation_one('Estar', ['TI33_25'], 'TI33_25', 'Exp', [6])",
        "validation_one('Estar', ['TI33_25'], 'TI33_25', 'Exp', [8])",
        "validation_one('Estar', ['TI33_25'], 'TI33_25', 'Exp', [10])",
        "validation_one('Estar', ['TI33_25'], 'TI33_25', 'Exp', [20])",
        "validation_one('sigma_y', ['TI33_25'], 'TI33_25', 'Exp', [1])",
        "validation_one('sigma_y', ['TI33_25'], 'TI33_25', 'Exp', [2])",
        "validation_one('sigma_y', ['TI33_25'], 'TI33_25', 'Exp', [3])",
        "validation_one('sigma_y', ['TI33_25'], 'TI33_25', 'Exp', [4])",
        "validation_one('sigma_y', ['TI33_25'], 'TI33_25', 'Exp', [5])",
        "validation_one('sigma_y', ['TI33_25'], 'TI33_25', 'Exp', [6])",
        "validation_one('sigma_y', ['TI33_25'], 'TI33_25', 'Exp', [8])",
        "validation_one('sigma_y', ['TI33_25'], 'TI33_25', 'Exp', [10])",
        "validation_one('sigma_y', ['TI33_25'], 'TI33_25', 'Exp', [20])"
        '''