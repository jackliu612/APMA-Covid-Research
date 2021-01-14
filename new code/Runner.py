from Tree import *
from Distribution import *
import statistics
import numpy as np

dP_range = np.arange(.8, 1.01, .1)
cT_range = np.arange(.6, 1.01, .01)

batches = 5
batchSize = 100
steps = 14
with open('b1.txt', 'a') as file:
    for dP in dP_range:
        print(dP)
        for cT in cT_range:
            print(cT)
            data = []
            for x in range(batches):
                success = 0
                for i in range(batchSize):
                    t = Tree(infectionProb=.5, detectionProb=dP, tracingProb=cT, b=1)
                    for s in range(steps):
                        t.step()
                        if t.isDone():
                            success += 1
                            break
                        if t.numNodes() > 10000:
                            break
                data.append(success / batchSize * 100)
                print(str(success / batchSize * 100) + '%')
            file.write('{:.2f}, '.format(statistics.mean(data)))
            # file.write('{:.2f}, '.format(statistics.stdev(data)))

            print('---------- FINAL RESULTS ----------')
            print('Mean:\t{}%'.format(statistics.mean(data)))
            print('SD:\t\t{}'.format(statistics.stdev(data)))
            print('-----------------------------------')
        file.write('\n')
