import multiprocessing
from multiprocessing import Pool
import numpy as np
import nn

def run_main(arg):
    nn.main(arg)

if __name__ == '__main__':

    arguments = np.array([
        "validation_FEM('Estar', 'TI33_Berkovich', 'TI33_25', 10)",
        "validation_FEM('Estar', 'TI33_Berkovich', 'TI33_25', 23)"
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
        
        ''',
        "validation_FEM('sigma_y', 'TI33_Berkovich', 'TI33_25', 10)",
        "validation_FEM('sigma_y', 'TI33_Berkovich', 'TI33_25', 20)"

        "validation_FEM('sigma_y', 'TI33_conical_70.3', 'TI33_25',2)",
        "validation_FEM('sigma_y', 'TI33_conical_70.3', 'TI33_25',4)",
        "validation_FEM('sigma_y', 'TI33_conical_70.3', 'TI33_25',6)",
        "validation_FEM('sigma_y', 'TI33_conical_70.3', 'TI33_25',8)",
        "validation_FEM('sigma_y', 'TI33_conical_70.3', 'TI33_25',10)",
        "validation_FEM('sigma_y', 'TI33_conical_70.3', 'TI33_25',12)",
        "validation_FEM('sigma_y', 'TI33_conical_70.3', 'TI33_25',14)",
        "validation_FEM('sigma_y', 'TI33_conical_70.3', 'TI33_25',16)",
        "validation_FEM('Estar', 'TI33_conical_70.3', 'TI33_25', 2)",
        "validation_FEM('Estar', 'TI33_conical_70.3', 'TI33_25', 4)",
        "validation_FEM('Estar', 'TI33_conical_70.3', 'TI33_25', 6)",
        "validation_FEM('Estar', 'TI33_conical_70.3', 'TI33_25', 8)",
        "validation_FEM('Estar', 'TI33_conical_70.3', 'TI33_25', 10)",
        "validation_FEM('Estar', 'TI33_conical_70.3', 'TI33_25', 12)",
        "validation_FEM('Estar', 'TI33_conical_70.3', 'TI33_25', 14)",
        "validation_FEM('Estar', 'TI33_conical_70.3', 'TI33_25', 16)"
        
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