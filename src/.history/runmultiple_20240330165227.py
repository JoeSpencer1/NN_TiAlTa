import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 0, '3D_quad', 0, '2D_70_quad', 0)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 1, '3D_quad', 1, '2D_70_quad', 1)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 2, '3D_quad', 2, '2D_70_quad', 2)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 3, '3D_quad', 3, '2D_70_quad', 3)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 4, '3D_quad', 4, '2D_70_quad', 4)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 5, '3D_quad', 5, '2D_70_quad', 5)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 6, '3D_quad', 6, '2D_70_quad', 6)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 8, '3D_quad', 8, '2D_70_quad', 8)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 10, '3D_quad', 10, '2D_70_quad', 10)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 15, '3D_quad', 15, '2D_70_quad', 15)"
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
