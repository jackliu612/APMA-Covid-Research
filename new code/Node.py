import numpy.random as random
from Distribution import *

_id = 0


class Node:
    test = 0
    """
        Node class that represents a single individual in the network
    """

    def __init__(self, parent=None, infected=False, quarantine=False, detectionProb=0.8, infectionProb=0.5, tracingProb=0.75, b=2, distribution=Poisson(3)):
        global _id
        self.tracable = []
        self.untracable = []
        self.id = _id
        _id = _id + 1
        self.parent = parent
        self.age = 0
        self.quarantine = quarantine
        self.infected = infected
        self.detectionProb = detectionProb
        self.infectionProb = infectionProb
        self.tracingProb = tracingProb
        self.b = b
        self.distribution = distribution

    def traceBack(self, complete=False, verbose=False):
        """
        Backwards tracing method tries to keep going back parents until it can't find one
        """
        cur = self
        prt = self.parent
        if verbose:
            print('--Tracing back on {}'.format(cur.id))
        while prt and cur in prt.tracable:
            cur = prt
            prt = cur.parent
            if verbose:
                print('--{} traced back to {}'.format(cur.id, prt.id))
            if not prt:
                break
        return cur

    def traceForward(self, complete=False, verbose=False):
        """
        Contact tracing method. Takes in a parameter to do a complete tracing or not (whether to have broken links)
        """
        if self.infected and not self.quarantine:  # Tracing testing probability
            if verbose:
                print('--{} traced'.format(self.id))
            self.quarantine = True
            for child in self.tracable:
                if complete or random.rand() < self.detectionProb:
                    child.traceForward(complete=complete, verbose=verbose)
                # child.traceForward(complete=complete, verbose=verbose)
            if complete:
                for child in self.untracable:
                    child.traceForward(complete=complete, verbose=verbose)

    def step(self, verbose=False):
        """
        Method run every time step. Returns a list of new children added
        """
        newChildren = []
        if not self.quarantine:
            # Contact Tracing
            if self.infected and self.age >= self.b and random.rand() < self.detectionProb:  # Detection prob
                if verbose:
                    print('{} was detected!'.format(self.id))
                self.traceBack(verbose=verbose).traceForward(verbose=verbose)
            # Recovery
            if self.age > 7:
                if verbose:
                    print('{} recovered'.format(self.id))
                self.quarantine = True
            # Spread
            if not self.quarantine and self.age <= self.b:
                num = self.distribution.next()
                for i in range(num):
                    newChildren.append(self.addChild(verbose))
        self.age = self.age + 1
        return newChildren

    def addChild(self, verbose=False):
        """
        Creates a new child and returns it
        """
        infected = True if self.infected and random.rand() < self.infectionProb else False
        child = Node(self, infected, False, self.detectionProb, self.infectionProb, self.tracingProb, self.b, self.distribution)
        if random.rand() < self.tracingProb:  # Alpha - contact tracing probability
            self.tracable.append(child)
            if verbose:
                print('{} ===> {}'.format(self.id, child.id) + ("*" if child.infected else ""))
        else:
            self.untracable.append(child)
            if verbose:
                print('{} -/-> {}'.format(self.id, child.id) + ("*" if child.infected else ""))
        return child

    def numNodes(self):
        num = 1
        for child in self.tracable + self.untracable:
            num = num + child.numNodes()
        return num

    def numInfected(self):
        num = 0
        if self.infected:
            num = num + 1
        for child in self.tracable + self.untracable:
            num = num + child.numInfected()
        return num

    def numQuarantined(self):
        num = 0
        if self.quarantine:
            num = num + 1
        for child in self.tracable + self.untracable:
            num = num + child.numQuarantined()
        return num

    def numUninfected(self):
        num = 0
        if not self.infected:
            num = num + 1
        for child in self.tracable + self.untracable:
            num = num + child.numUninfected()
        return num

    def rVal(self):
        if self.infected and self.age != 0:
            count = 0
            for child in self.tracable + self.untracable:
                if child.infected:
                    count = count + 1
            return count
        else:
            return -1

    def __str__(self):
        return '<id={}, trace={}, untrace={}, infected={}, quarentine={}>'.format(self.id, self.tracable, self.untracable, self.infected, self.quarantine)

    def __repr__(self):
        return '<id={}, infected={}, quarantine={}>'.format(self.id, self.infected, self.quarantine)
