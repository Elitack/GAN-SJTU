import random
import numpy as np
import pandas as pd
import os
import networkx as nx
import sys
from conf import *

data_dir = 'Data/'


class Datum:
    def __init__(self):
        pass

    def get_data(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.matrix = np.load(data_dir+'TargetMatrix_{}_{}.npy'.format(start_date, end_date))
        self.dim = self.matrix.shape[0]

    def get_batch(self, batch_size):
        idx = np.random.choice(self.dim, size=batch_size, replace=False)
        batch = self.matrix[idx, :]
        return batch
            

            

        
if __name__ == "__main__":
    data = Datum()