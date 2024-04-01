import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 0, '3D_quad', 25, '2D_70_quad', 25)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 1, '3D_quad', 25, '2D_70_quad', 25)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 2, '3D_quad', 25, '2D_70_quad', 25)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 3, '3D_quad', 25, '2D_70_quad', 25)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 4, '3D_quad', 25, '2D_70_quad', 25)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 5, '3D_quad', 25, '2D_70_quad', 25)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 6, '3D_quad', 25, '2D_70_quad', 25)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 8, '3D_quad', 25, '2D_70_quad', 25)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 10, '3D_quad', 25, '2D_70_quad', 25)",
        "validation_three('sigma_y', 'TI33_25', 'TI33_25', 15, '3D_quad', 25, '2D_70_quad', 25)"
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
