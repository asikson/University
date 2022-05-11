class Node:
    def __init__(self, C, F, M):
        self.C = C
        self.F = F
        self.M = M

np = 5
nv = 4

# physical network
physicalNodes = [
    Node(6, 3.0, 8000),
    Node(4, 2.6, 4000),
    Node(2, 3.2, 4000),
    Node(4, 2, 8000),
    Node(6, 2.4, 6000)
]

physicalLinks = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

physicalCapacities = [
    [0, 500, 500, 0, 0],
    [500, 0, 0, 500, 500],
    [500, 0, 0, 500, 0],
    [0, 500, 500, 0, 500],
    [0, 500, 0, 500, 0]
]

# virtual network
virtualNodes = [
    Node(2, 2.6, 64),
    Node(3, 2.2, 256),
    Node(2, 2, 128),
    Node(2, 2.6, 512)
]

virtualLinks = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

virtualCapacities = [
    [0, 2.048, 8.448, 0],
    [2.048, 0, 0, 2.048],
    [8.448, 0, 0, 34.368],
    [0, 34.368, 2.048, 0]
]