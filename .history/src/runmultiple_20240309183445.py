import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([
        "validation_one('sigma_y', 1, '2D_70', '2D_70')",
        "validation_one('sigma_y', 2, '2D_70', '2D_70')",
        "validation_one('sigma_y', 3, '2D_70', '2D_70')",
        "validation_one('sigma_y', 4, '2D_70', '2D_70')",
        "validation_one('sigma_y', 5, '2D_70', '2D_70')",
        "validation_one('sigma_y', 6, '2D_70', '2D_70')",
        "validation_one('sigma_y', 8, '2D_70', '2D_70')",
        "validation_one('sigma_y', 10, '2D_70', '2D_70')",
        "validation_one('sigma_y', 15, '2D_70', '2D_70')",
        "validation_one('sigma_y', 20, '2D_70', '2D_70')"
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
    with open('output.txt', 'a') as f:
        f.write('\n')
        '''
        "validation_one('sigma_y', 1, '3D_linear', '3D_linear')"

        '''
        '''

        (All 3 data types)
        "validation_three('sigma_y', 0, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 0, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 1, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 1, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 2, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 2, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 3, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 3, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 4, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 4, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 5, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 5, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 6, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 6, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 8, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 8, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 10, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 10, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 20, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 20, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')"   
        
        (2 data types)
        "validation_two('sigma_y', 0, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 0, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 1, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 1, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 2, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 2, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 3, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 3, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 4, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 4, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 5, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 5, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 6, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 6, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 8, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 8, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 10, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 10, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 20, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 20, 'TI33_3D', 'TI33_25', 'TI33_25')"
        
        (1 data type)  
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 1)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 1)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 2)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 2)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 3)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 3)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 4)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 4)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 5)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 5)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 6)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 6)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 8)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 8)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 10)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 10)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 20)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 20)"
        '''