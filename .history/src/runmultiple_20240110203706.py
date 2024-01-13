import multiprocessing
import numpy as np
import nn

def run_main(arg):
    nn.main(arg)

if __name__ == '__main__':

    arguments = np.array([
        "validation_two('Estar', 1, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('Estar', 2, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('Estar', 3, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('Estar', 4, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('Estar', 5, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('Estar', 6, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('Estar', 8, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('Estar', 10, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('Estar', 20, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('sigma_y', 1, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('sigma_y', 2, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('sigma_y', 3, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('sigma_y', 4, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('sigma_y', 5, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('sigma_y', 6, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('sigma_y', 8, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('sigma_y', 10, 'TI33_25', 'Berk', 'Exp', lay=1)",
        "validation_two('sigma_y', 20, 'TI33_25', 'Berk', 'Exp', lay=1)"
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
        
        '''

        '''
        "validation_two('Estar', 1, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('Estar', 2, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('Estar', 3, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('Estar', 4, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('Estar', 5, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('Estar', 6, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('Estar', 8, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('Estar', 10, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('Estar', 20, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('sigma_y', 1, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('sigma_y', 2, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('sigma_y', 3, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('sigma_y', 4, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('sigma_y', 5, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('sigma_y', 6, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('sigma_y', 8, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('sigma_y', 10, 'TI33_25', 'FEM', 'Exp')",
        "validation_two('sigma_y', 20, 'TI33_25', 'FEM', 'Exp')"
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