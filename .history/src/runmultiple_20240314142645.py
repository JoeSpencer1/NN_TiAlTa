import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn
import os

def run_main(arg):
    nn.main(arg)


if __name__ == '__main__':

    arguments = np.array([
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
        "validation_three('Er', 'Lu et al/B3090', 'Lu et al/B3090', 100, 'Lu et al/Berkovich', 14, 'Lu et al/FEM_70deg', 100, typ='hi')",
        "validation_three('sigma_y', 'Lu et al/B3090', 'Lu et al/B3090', 100, 'Lu et al/Berkovich', 14, 'Lu et al/FEM_70deg', 100, typ='hi')",
        "validation_three('Er', 'Lu et al/B3090', 'Lu et al/B3090', 100, 'Lu et al/Berkovich', 14, 'Lu et al/FEM_70deg', 100, typ='lo')",
        "validation_three('sigma_y', 'Lu et al/B3090', 'Lu et al/B3090', 100, 'Lu et al/Berkovich', 14, 'Lu et al/FEM_70deg', 100, typ='lo')"
        '''