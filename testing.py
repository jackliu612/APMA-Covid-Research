from Node import *
from Tree import *

t = Tree(10)
print(t)
for i in range(80):
    t.step()
    print(t)