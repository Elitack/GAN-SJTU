import pandas as pd
import pickle
import numpy as np

df = pd.read_csv('guarantee.csv', index_col=0)

target_start_date = '2014-01-01'
target_end_date = '2016-01-01'

CompanyIndex = pickle.load(open('CompanyIndex.list', 'rb'), encoding='latin1')
length = len(CompanyIndex)

target_matrix = np.zeros((length, length))
count = 0
for index, row in df.iterrows():
    if row['start_time'] >= target_start_date and row['start_time'] <= target_end_date:
        start_idx = CompanyIndex.index(row['start_node'])
        end_idx = CompanyIndex.index(row['end_node'])
        target_matrix[start_idx, end_idx] = row['amt']
        count += 1

np.save('TargetMatrix_{}_{}.npy'.format(target_start_date, target_end_date), target_matrix)