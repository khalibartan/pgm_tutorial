from itertools import product
from pgmpy.factors.discrete import JointProbabilityDistribution

with open('joint.dat', 'r') as f:
    x = f.read()

x = x.split('\n')
del x[-1]
x = list(map(lambda i: i.split('\t'), x))

for i in range(len(x)):
    x[i] = [int(x[i][0]), float(x[i][1])]

y = [(0, 1) for i in range(12)]
dit = {}

for i in product(*y):
    dit[i] = 1

for i in x:
    y= [0 for j in range(12)]
    x = list(reversed(bin(i[0])))[:-2]
    x = list(map(int, x))
    for j in range(len(x)):
        y[j] = x[j]
    y = tuple(y)
    dit[y] = i[1]

probs = []
y = [(0, 1) for i in range(12)]
for i in product(*y):
    probs.append(dit[i])
