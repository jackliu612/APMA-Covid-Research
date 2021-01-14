import numpy.random as random


class Distribution:
    def __init__(self):
        pass

    def next(self):
        return 0


class Poisson:
    def __init__(self, mean):
        self.mean = mean

    def next(self):
        return random.poisson(lam=self.mean)


class Uniform:
    def __init__(self, mean):
        self.mean = mean

    def next(self):
        return random.randint(self.mean * 2 + 1)


class Constant:
    def __init__(self, mean):
        self.mean = mean

    def next(self):
        return self.mean
