class UnionFind:
    def __init__(self):
        self.parents = {}
        self.sizes = {}

    def createSet(self, value):
        if value in self.parents:
            return
        self.parents[value] = value
        self.sizes[value] = 1

    def find(self, value):
        if value not in self.parents:
            return
        if self.parents[value] != value:
            self.parents[value] = self.find(self.parents[value])
        return self.parents[value]

    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents or valueTwo not in self.parents:
            return
        valueOne = self.find(valueOne)
        valueTwo = self.find(valueTwo)
        if valueOne == valueTwo:
            return
        if self.sizes[valueTwo] > self.sizes[valueOne]:
            valueOne, valueTwo = valueTwo, valueOne
        self.parents[valueTwo] = valueOne
        self.sizes[valueOne] += self.sizes[valueTwo]
