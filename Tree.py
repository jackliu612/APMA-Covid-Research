from Node import Node
class Tree:
    def __init__(self, num):
        self.root = Node(infected=True)
        self.activation = [self.root]

    def __str__(self):
        return 'Node Count: {}, Infected: {}, Quarentined: {}, Uninfected: {}'.format(self.numNodes(), self.numInfected(), self.numQuarentined(), self.numUninfected())
    def step(self):
        newActivation = self.activation
        for node in self.activation:
            if node.infected:
                newActivation = newActivation + node.step()
        self.activation = newActivation
    
    def numNodes(self):
        return self.root.numNodes()

    def numInfected(self):
        return self.root.numInfected()
    
    def numQuarentined(self):
        return self.root.numQuarentined()
    
    def numUninfected(self):
        return self.root.numUninfected()
