# batch run test

#import mesa
import mesa
from mesa.datacollection import DataCollector
print("Mesa loaded from:", mesa.__file__)
from mesa.batchrunner import batch_run
import numpy as np
from partymodel import PartyModel
import json
from mpi4py import MPI

params_dict = {0: {'alcohol_prop': 0.1, 'p': np.arange(0.01, 0.06, 0.01)}, 
               1: {'alcohol_prop': 0.1, 'p': np.arange(0.06, 0.11, 0.01)},
               2: {'alcohol_prop': 0.2, 'p': np.arange(0.01, 0.06, 0.01)}, 
               3: {'alcohol_prop': 0.2, 'p': np.arange(0.06, 0.11, 0.01)},
               4: {'alcohol_prop': 0.3, 'p': np.arange(0.01, 0.06, 0.01)}, 
               5: {'alcohol_prop': 0.3, 'p': np.arange(0.06, 0.11, 0.01)},
               6: {'alcohol_prop': 0.4, 'p': np.arange(0.01, 0.06, 0.01)}, 
               7: {'alcohol_prop': 0.4, 'p': np.arange(0.06, 0.11, 0.01)},
               8: {'alcohol_prop': 0.5, 'p': np.arange(0.01, 0.06, 0.01)}, 
               9: {'alcohol_prop': 0.5, 'p': np.arange(0.06, 0.11, 0.01)},
               10: {'alcohol_prop': 0.6, 'p': np.arange(0.01, 0.06, 0.01)}, 
               11: {'alcohol_prop': 0.6, 'p': np.arange(0.06, 0.11, 0.01)},
               12: {'alcohol_prop': 0.7, 'p': np.arange(0.01, 0.06, 0.01)}, 
               13: {'alcohol_prop': 0.7, 'p': np.arange(0.06, 0.11, 0.01)},
               14: {'alcohol_prop': 0.8, 'p': np.arange(0.01, 0.06, 0.01)}, 
               15: {'alcohol_prop': 0.8, 'p': np.arange(0.06, 0.11, 0.01)},
               16: {'alcohol_prop': 0.9, 'p': np.arange(0.01, 0.06, 0.01)}, 
               17: {'alcohol_prop': 0.9, 'p': np.arange(0.06, 0.11, 0.01)},
               18: {'alcohol_prop': 1.0, 'p': np.arange(0.01, 0.06, 0.01)}, 
               19: {'alcohol_prop': 1.0, 'p': np.arange(0.06, 0.11, 0.01)},}


if __name__=="__main__":

    rank = comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    params = {'neighbor_dance_thres':np.linspace(0.1, 1, 10),
            'alcohol_dance_thres': range(2, 5),
            'energy':15,
            'alcohol_prop':params_dict[rank]['alcohol_prop'],
            'extro_floor':0,
            'extro_ceiling':1,
            'k': range(2,16),
            'p': params_dict[rank]['p'],
            'network_type':"wattsstrogatz",
            'seed':[0,2,4,6,8,10]}

    results = batch_run(
    PartyModel,
    params,
    iterations = 1,
    max_steps = 100,
    #data_collection_period = 1,
    #number_processes = 10
    )

    with open(f'json_folder/batch_test_midway_{rank}.json', 'w') as f:
        json.dump(results, f)

    print('all done!')