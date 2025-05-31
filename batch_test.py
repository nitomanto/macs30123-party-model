# batch run test

#import mesa
import mesa
from mesa.datacollection import DataCollector
print("Mesa loaded from:", mesa.__file__)
from mesa.batchrunner import batch_run
import numpy as np
from partymodel import PartyModel
import json
import pandas as pd
#from mpi4py import MPI

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

    params = {'neighbor_dance_thres': 0.5,
            'alcohol_dance_thres': range(2, 5),
            'energy':15,
            'alcohol_prop':[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
            'extro_floor':0,
            'extro_ceiling':1,
            'k': range(2,16),
            'p': np.arange(0.01, 0.11, 0.01),
            'network_type':"wattsstrogatz",
            'seed':range(0, 20)}

    results = batch_run(
    PartyModel,
    params,
    iterations = 1,
    max_steps = 100,
    #data_collection_period = 1,
    number_processes = 20
    )

    df = pd.DataFrame(results)
    df.to_csv('batch_test.csv')

    print('all done!')