import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([
        "validation_one('sigma_y', 10, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('Estar', 10, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('sigma_y', 20, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('Estar', 20, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('sigma_y', 30, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('Estar', 30, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('sigma_y', 40, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('Estar', 40, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('sigma_y', 50, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('Estar', 50, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('sigma_y', 60, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('Estar', 60, 'TI33_2D_70.3', 'TI33_2D_70.3')",
        "validation_one('sigma_y', 10, 'TI33_3D', 'TI33_3D')",
        "validation_one('Estar', 10, 'TI33_3D', 'TI33_3D')",
        "validation_one('sigma_y', 20, 'TI33_3D', 'TI33_3D')",
        "validation_one('Estar', 20, 'TI33_3D', 'TI33_3D')",
        "validation_one('sigma_y', 30, 'TI33_3D', 'TI33_3D')",
        "validation_one('Estar', 30, 'TI33_3D', 'TI33_3D')",
        "validation_one('sigma_y', 40, 'TI33_3D', 'TI33_3D')",
        "validation_one('Estar', 40, 'TI33_3D', 'TI33_3D')",
        "validation_one('sigma_y', 50, 'TI33_3D', 'TI33_3D')",
        "validation_one('Estar', 50, 'TI33_3D', 'TI33_3D')",
        "validation_one('sigma_y', 60, 'TI33_3D', 'TI33_3D')",
        "validation_one('Estar', 60, 'TI33_3D', 'TI33_3D')",
        "validation_one('sigma_y', 10, 'TI33_25', 'TI33_25')",
        "validation_one('Estar', 10, 'TI33_25', 'TI33_25')",
        "validation_one('sigma_y', 20, 'TI33_25', 'TI33_25')",
        "validation_one('Estar', 20, 'TI33_25', 'TI33_25')",
        "validation_one('sigma_y', 30, 'TI33_25', 'TI33_25')",
        "validation_one('Estar', 30, 'TI33_25', 'TI33_25')",
        "validation_one('sigma_y', 40, 'TI33_25', 'TI33_25')",
        "validation_one('Estar', 40, 'TI33_25', 'TI33_25')",
        "validation_one('sigma_y', 50, 'TI33_25', 'TI33_25')",
        "validation_one('Estar', 50, 'TI33_25', 'TI33_25')",
        "validation_one('sigma_y', 60, 'TI33_25', 'TI33_25')",
        "validation_one('Estar', 60, 'TI33_25', 'TI33_25')"
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
        "validation_three('sigma_y', 0, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 0, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 1, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 1, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 2, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 2, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 3, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 3, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 4, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 4, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 5, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 5, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 6, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 6, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 8, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 8, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 10, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 10, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 20, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Estar', 20, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')"   
        
        (2 data types)
        "validation_two('sigma_y', 0, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 0, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 1, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 1, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 2, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 2, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 3, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 3, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 4, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 4, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 5, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 5, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 6, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 6, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 8, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 8, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 10, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 10, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 20, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Estar', 20, 'TI33_3D', 'TI33_25', 'TI33_25')"
        
        (1 data type)  

        ('TI33_2D_70.3', 'TI33_2D_60', 'TI33_2D_45', 'TI33_2D_30')
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 1)",
        "validation_one('Estar', 'TI33_2D_70.3', 'TI33_2D_70.3', 1)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 2)",
        "validation_one('Estar', 'TI33_2D_70.3', 'TI33_2D_70.3', 2)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 3)",
        "validation_one('Estar', 'TI33_2D_70.3', 'TI33_2D_70.3', 3)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 4)",
        "validation_one('Estar', 'TI33_2D_70.3', 'TI33_2D_70.3', 4)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 5)",
        "validation_one('Estar', 'TI33_2D_70.3', 'TI33_2D_70.3', 5)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 6)",
        "validation_one('Estar', 'TI33_2D_70.3', 'TI33_2D_70.3', 6)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 8)",
        "validation_one('Estar', 'TI33_2D_70.3', 'TI33_2D_70.3', 8)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 10)",
        "validation_one('Estar', 'TI33_2D_70.3', 'TI33_2D_70.3', 10)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 20)",
        "validation_one('Estar', 'TI33_2D_70.3', 'TI33_2D_70.3', 20)"
        
        '''