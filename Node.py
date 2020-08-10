import numpy.random as random
id = 0

class Node: 
    """
        Node class that represents a single individual in the network
    """
    def __init__(self, _id=-1, parent=None, infected=False, age=0, quarentine=False):
        self.tracable = []
        self.untracable = []
        self.id = _id
        self.parent = parent
        self.age = age
        self.quarentine = quarentine
        self.infected = infected
    
    def trace(self, complete=False):
        """
        Contact tracing method. Takes in a parameter to do a complete tracing or not (whether to have broken links)
        """
        if self.infected and not self.quarentine:   #Tracing testing probability
            self.quarentine = True
            for child in self.tracable:
                child.trace(complete)
            if complete:
                for child in self.untracable:
                    child.trace(complete)

    def step(self):
        """
        Method run every time step. Returns a list of new children added
        """
        newChildren = []
        if not self.quarentine:
            #Contact Tracing
            if self.infected and self.age > 2:  #Detection prob
                self.trace(False)
            #Recovery
            if self.age > 7:
                self.infected = False
            #Spread
            if not self.quarentine:
                num = random.poisson(lam=3)
                for i in range(num):
                    newChildren.append(self.addChild())
        self.age = self.age + 1
        return newChildren


    def addChild(self, _id=-1):
        """
        Creates a new child and returns it
        """
        infected = True if self.infected and random.rand() < 0.5 else False
        child = Node(_id, self, infected, 0, False)
        if random.rand() < 0.85:    # Alpha - contact tracing probability
            self.tracable.append(child)
        else:
            self.untracable.append(child)
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

    def numQuarentined(self):
        num = 0
        if self.quarentine:
            num = num + 1
        for child in self.tracable + self.untracable:
            num = num + child.numQuarentined()
        return num

    def numUninfected(self):
        num = 0
        if not self.infected:
            num = num + 1
        for child in self.tracable + self.untracable:
            num = num + child.numUninfected()
        return num

    def __str__(self):
        return '<id={}, trace={}, untrace={}, infected={}, quarentine={}>'.format(self.id, self.tracable, self.untracable, self.infected, self.quarentine)
    
    def __repr__(self):
        return '<id={}, infected={}, quarentine={}>'.format(self.id, self.infected, self.quarentine)
