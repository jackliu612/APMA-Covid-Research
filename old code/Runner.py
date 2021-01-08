from Tree import *
import statistics

batches = 5
batchSize = 100
steps = 14
with open('contacts.txt', 'a') as other:
    with open('out6.txt', 'a') as file:
        for dP in range(80, 101, 1):
            print(dP)
            for cT in range(60, 101, 1):
                print(cT)
                data = []
                contacts = []
                for x in range(batches):
                    success = 0
                    for i in range(batchSize):
                        t = Tree(infectionProb=.5, detectionProb=(dP / 100), tracingProb=(cT / 100))
                        for s in range(steps):
                            t.step()
                            if t.isDone():
                                success += 1
                                contacts.append(t.numNodes())
                                break
                            if t.numNodes() > 10000:
                                break
                    data.append(success / batchSize * 100)
                    print(str(success / batchSize * 100) + '%')
                file.write('{:.2f}, '.format(statistics.mean(data)))
                file.write('{:.2f}, '.format(statistics.stdev(data)))

                other.write('{:.2f}, '.format(statistics.mean(contacts)))
                print('---------- FINAL RESULTS ----------')
                print('Mean:\t{}%'.format(statistics.mean(data)))
                print('SD:\t\t{}'.format(statistics.stdev(data)))
                print('-----------------------------------')
            file.write('\n')
