import node
import network as net

np = 5

physicalNodes = [
    node.Node(6, 3.0, 8000),
    node.Node(4, 2.6, 4000),
    node.Node(2, 3.2, 4000),
    node.Node(4, 2, 8000),
    node.Node(6, 2.4, 6000)
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

physicalNetwork = net.PhysicalNetwork(np, physicalNodes, physicalLinks, physicalCapacities)

nv = 4

virtualNodes = [
    node.Node(2, 2.6, 64),
    node.Node(3, 2.2, 256),
    node.Node(2, 2, 128),
    node.Node(2, 2.6, 512)
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

virtualNetwork = net.VirtualNetwork(nv, virtualNodes, virtualLinks, virtualCapacities)