from Node import Node
from Distribution import *


class Tree:
    def __init__(self, detectionProb=0.8, infectionProb=0.18, tracingProb=0.75, b=2, distribution=Poisson(3)):
        self.root = Node(infected=True, detectionProb=detectionProb, infectionProb=infectionProb, tracingProb=tracingProb, b=b, distribution=distribution)
        self.activation = [self.root]
        self.nodes = (1, 0)
        self.infected = (0, 1)
        self.uninfected = (0, 0)
        self.quarantined = (0, 0)
        self.r = (0, 0)
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
        if self.nodes[0] != self.day:
            self.nodes = (self.day, self.root.numNodes())
        return self.nodes[1]

    def numInfected(self):
        if self.infected[0] != self.day:
            self.infected = (self.day, self.root.numInfected())
        return self.infected[1]

    def numQuarantined(self):
        if self.quarantined[0] != self.day:
            self.quarantined = (self.day, self.root.numQuarantined())
        return self.quarantined[1]

    def numUninfected(self):
        if self.uninfected[0] != self.day:
            self.uninfected = (self.day, self.root.numUninfected())
        return self.uninfected[1]

    def rVal(self):
        if self.r[0] != self.day:
            inf = 0
            count = 0
            for node in self.activation:
                temp = node.rVal()
                if temp is not -1:
                    inf += temp
                    count += 1
            self.r = (self.day, (inf / count if count != 0 else 0))
        return self.r[1]

    def isDone(self):
        return self.numInfected() == self.numQuarantined()
