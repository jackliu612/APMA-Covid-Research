from Node import Node


class Tree:
    def __init__(self, num):
        self.root = Node(infected=True)
        self.activation = [self.root]
        self.day = 0

    def __str__(self):
        return '**Day {}: Node Count: {}, Infected: {}, Quarantined: {}, Uninfected: {}, R: {}'.format(self.day, self.numNodes(), self.numInfected(), self.numQuarantined(), self.numUninfected(),
                                                                                                       self.rVal())

    def step(self, verbose=False):
        newActivation = self.activation
        for node in self.activation:
            if node.infected:
                newActivation = newActivation + node.step(verbose)
        self.activation = newActivation
        self.day = self.day + 1

    def numNodes(self):
        return self.root.numNodes()

    def numInfected(self):
        return self.root.numInfected()

    def numQuarantined(self):
        return self.root.numQuarantined()

    def numUninfected(self):
        return self.root.numUninfected()

    def rVal(self):
        inf = 0
        count = 0
        for node in self.activation:
            temp = node.rVal()
            if temp is not -1:
                inf += temp
                count += 1
        return inf / count if count != 0 else 0
