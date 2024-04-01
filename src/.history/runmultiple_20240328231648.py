import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([
        "validation_three('Er', 'TI33_25', 'TI33_25', 0, '3D_linear_r', 0, '2D_70_linear_r', 0, typ='lo')",
        "validation_three('Er', 'TI33_25', 'TI33_25', 1, '3D_linear_r', 1, '2D_70_linear_r', 1, typ='lo')",
        "validation_three('Er', 'TI33_25', 'TI33_25', 2, '3D_linear_r', 2, '2D_70_linear_r', 2, typ='lo')",
        "validation_three('Er', 'TI33_25', 'TI33_25', 3, '3D_linear_r', 3, '2D_70_linear_r', 3, typ='lo')",
        "validation_three('Er', 'TI33_25', 'TI33_25', 4, '3D_linear_r', 4, '2D_70_linear_r', 4, typ='lo')",
        "validation_three('Er', 'TI33_25', 'TI33_25', 5, '3D_linear_r', 5, '2D_70_linear_r', 5, typ='lo')",
        "validation_three('Er', 'TI33_25', 'TI33_25', 6, '3D_linear_r', 6, '2D_70_linear_r', 6, typ='lo')",
        "validation_three('Er', 'TI33_25', 'TI33_25', 8, '3D_linear_r', 8, '2D_70_linear_r', 8, typ='lo')",
        "validation_three('Er', 'TI33_25', 'TI33_25', 10, '3D_linear_r', 10, '2D_70_linear_r', 10, typ='lo')",
        "validation_three('Er', 'TI33_25', 'TI33_25', 15, '3D_linear_r', 15, '2D_70_linear_r', 15, typ='lo')"
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
