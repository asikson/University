class Node:
    def __init__(self, C, F, M):
        self.C = C
        self.F = F
        self.M = M

    def meetsConstraints(self, node):
        return (node.C <= self.C
            and node.F <= self.F 
            and node.M <= self.M)