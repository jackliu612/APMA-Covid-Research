import statistics

from Node import *
from Tree import *

t = Tree(tracingProb=0.3)
print(t)
for i in range(15):
    t.step(False)
    print(t)
    if t.isDone() or t.numNodes()>10000:
        break
# with open('out.txt', 'w') as f:
#     test = [1.2, 4.2, 3.14, 2.7, 6.9]
#     f.write('{:.2f}, '.format(statistics.mean(test)))
#     f.write('hi')
#     f.write('bye')
