import pandas as pd
from collections import Counter
from math import log
import pdb

data = pd.read_csv('bank.csv')

### Entropy Function 

def entropy(dataColumn):
    '''
        Receive data of column in list to calculate the Entropy 
    '''
    k = Counter(list(dataColumn)).keys()
    v = Counter(dataColumn).values()
    l = len(dataColumn)
    
    base = 2 if len(k) < 2 else len(k)
    E = [(-(i/l)*log(i/l, base)) for i in v]
    return sum(E)


def decideSplitFeature(dataTable):
    '''
        Provide a data-set and it returns the splitting feature, on which further decision node is formed
    '''
    max = float('-inf')
    attribute = ''

    for obj in data.columns:
        tmp = entropy(list(data[obj]))  
        if tmp > max:
            max = tmp
            attribute = obj 
        else:
            max
    print(f"Max entropy is {max} find for '{attribute}'.")
    return (attribute, max)


columns = list(data.columns) 

# for attr in data.columns:
weighted_avg = 0
total_case = len(data['age'])
for k,v in data.groupby('age'):
    E = entropy(v['deposit'])
    print(f"Entropy for case {k} is calculated: {E}")
    weighted_avg += (len(v)/total_case)*E
    
    
    



