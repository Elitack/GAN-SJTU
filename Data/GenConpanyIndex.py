import pandas as pd
import pickle

df = pd.read_csv('guarantee.csv', index_col=0)
CompanyIndex = []

for index, row in df.iterrows():
    if row['start_node'] not in CompanyIndex:
        CompanyIndex.append(row['start_node'])
    if row['end_node'] not in CompanyIndex:
        CompanyIndex.append(row['end_node'])        
    if index % 1000 == 0:
        print(index)

pickle.dump(CompanyIndex, open('CompanyIndex.list', "wb" ))