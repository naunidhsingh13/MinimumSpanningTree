
# Implementation of Graph


class WeightedGraph:

    # Edges have weights
    # vertices can be str or int
    # Undirected
    def __init__(self):
        self.weights = dict()
        self.nodes = set()

    def load(self, nodes: list[list]):
        """
        :param nodes: List[List(3) ...]
        :return:
        """
        for u, v, w in nodes:
            if u > v:
                u, v = v, u
            self.weights[(u, v)] = w
            self.nodes.add(u)
            self.nodes.add(v)

    def weight(self, u, v):

        if u > v:
            u, v = v, u

        if (u, v) in self.weights:
            return self.weights[(u, v)]

        else:
            return None
