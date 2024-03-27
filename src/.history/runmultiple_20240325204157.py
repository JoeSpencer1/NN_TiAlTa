import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([
        "validation_one('Er', 'TI33_25', 'TI33_25', 5, n_vd=0.2)",
        "validation_one('Er', '3D_quad', '3D_quad', 5, n_vd=0.2)",
        "validation_one('Er', '3D_linear', '3D_linear', 5, n_vd=0.2)",
        "validation_one('sigma_y', 'TI33_25', 'TI33_25', 5, n_vd=0.2)",
        "validation_one('sigma_y', '3D_quad', '3D_quad', 5, n_vd=0.2)",
        "validation_one('sigma_y', '3D_linear', '3D_linear', 5, n_vd=0.2)"
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