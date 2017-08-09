import pandas as pd

with open('dataset.dat', 'r') as f:
    data = f.read()

data = data.split('\n')[:-1]
data = list(map(lambda i: int(i), data))
types = ['IsSummer','HasFlu','HasFoodPoisoning','HasHayFever','HasPneumonia',
        'HasRespiratoryProblems', 'HasGastricProblems', 'HasRash', 'Coughs',
        'IsFatigued', 'Vomits','HasFever']
dataset = []

for i in range(len(data)):
    row = list(reversed(bin(data[i])))[:-2]
    row.extend(['0' for j in range(len(row),12)])
    dataset.append(row)
    
dataset = pd.DataFrame(dataset, columns=types, dtype=str)
dataset.to_csv(path_or_buf='dataset.csv', index=False)
del data
del types


