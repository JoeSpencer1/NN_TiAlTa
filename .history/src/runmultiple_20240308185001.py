import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([
        "validation_two('sigma_y', 0, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 1, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 2, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 3, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 4, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 5, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 6, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 8, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 10, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 15, 'TI33_25', 'TI33_25', '3D_quad')",
        "validation_two('sigma_y', 20, 'TI33_25', 'TI33_25', '3D_quad')",
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
        '''
        '''

        (All 3 data types)
        "validation_three('sigma_y', 0, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 0, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 1, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 1, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 2, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 2, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 3, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 3, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 4, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 4, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 5, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 5, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 6, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 6, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 8, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 8, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 10, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 10, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('sigma_y', 20, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_three('Er', 20, 'TI33_2D_70.3', 'TI33_3D', 'TI33_25', 'TI33_25')"   
        
        (2 data types)
        "validation_two('sigma_y', 0, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 0, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 1, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 1, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 2, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 2, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 3, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 3, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 4, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 4, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 5, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 5, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 6, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 6, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 8, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 8, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 10, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 10, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('sigma_y', 20, 'TI33_3D', 'TI33_25', 'TI33_25')",
        "validation_two('Er', 20, 'TI33_3D', 'TI33_25', 'TI33_25')"
        
        (1 data type)  
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 1)",
        "validation_one('Er', 'TI33_2D_70.3', 'TI33_2D_70.3', 1)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 2)",
        "validation_one('Er', 'TI33_2D_70.3', 'TI33_2D_70.3', 2)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 3)",
        "validation_one('Er', 'TI33_2D_70.3', 'TI33_2D_70.3', 3)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 4)",
        "validation_one('Er', 'TI33_2D_70.3', 'TI33_2D_70.3', 4)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 5)",
        "validation_one('Er', 'TI33_2D_70.3', 'TI33_2D_70.3', 5)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 6)",
        "validation_one('Er', 'TI33_2D_70.3', 'TI33_2D_70.3', 6)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 8)",
        "validation_one('Er', 'TI33_2D_70.3', 'TI33_2D_70.3', 8)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 10)",
        "validation_one('Er', 'TI33_2D_70.3', 'TI33_2D_70.3', 10)",
        "validation_one('sigma_y', 'TI33_2D_70.3', 'TI33_2D_70.3', 20)",
        "validation_one('Er', 'TI33_2D_70.3', 'TI33_2D_70.3', 20)"
        '''