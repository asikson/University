import queue

class PhysicalNetwork:
    def __init__(self, n, nodes, links, capacities):
        self.n = n
        self.nodes = nodes
        self.links = links
        self.capacities = capacities

    def getLinkStress(self, v, u, bandwidth):
        return bandwidth / self.capacities[v][u]

    def getNeighbours(self, i):
        return list(filter(
            lambda x: self.links[i][x] == 1,
            list(range(self.n))
        ))
    def getCapacity(self, v, u):
        return self.capacities[v][u]

    def dijkstra(self, v, bandwidth):
        visited = []

        d = {i: float('inf') for i in range(self.n)}
        paths = dict()
        d[v] = (0)
        paths[v] = []

        pq = queue.PriorityQueue()
        pq.put((0, v))

        while not pq.empty():
            (dist, current) = pq.get()
            visited.append(current)
            neighbours = self.getNeighbours(current)
            neighbours = list(filter(
                lambda n: self.getCapacity(current, n) >= bandwidth,
                neighbours
            ))

            for n in neighbours:
                distance = self.getLinkStress(current, n, bandwidth)
                if n not in visited:
                    oldCost = d[n]
                    newCost = d[current] + distance
                    newPath = paths[current] + [(current, n)]
                    if newCost < oldCost:
                        pq.put((newCost, n))
                        d[n] = newCost
                        paths[n] = newPath

        return d, paths

    def getNodeStress(self, i):
        node = self.nodes[i]
        return node.F * (1 / (node.M * node.M) + 1 / (node.C * node.C))

    def getLinkPath(self, v, u, bandwidth):
        _, paths = self.dijkstra(v, bandwidth)
        return paths[u]
                
            
class VirtualNetwork:
    def __init__(self, n, nodes, links, capacities):
        self.n = n
        self.nodes = nodes
        self.links = links
        self.capacities = capacities
    
    def getNeighbours(self, j):
        return list(filter(
            lambda x: self.links[j][x] == 1,
            list(range(self.n))
        ))

    def getBandwidth(self, v, u):
        return self.capacities[v][u]