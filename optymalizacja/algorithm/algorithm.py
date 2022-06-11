import data
import costFunction as cf

beta = 0.001

def algorithm(physicalNetwork, virtualNetwork):

    np = physicalNetwork.n
    nv = virtualNetwork.n

    candidates = dict()
    physicalNodes = physicalNetwork.nodes
    virtualNodes = virtualNetwork.nodes
    for j in range(nv):
        physicalIndexes = list(range(np))
        candidates[j] = list(filter(
            lambda i: physicalNodes[i].meetsConstraints(virtualNodes[j]),
            physicalIndexes
        ))

    order = list(range(nv))
    order.sort(key=lambda i: len(candidates[i]))
    
    mapping = dict()
    links = dict()
    for j in order:
        neighbours = virtualNetwork.getNeighbours(j)
        pi = dict()

        for n in neighbours:
            bandwidth = virtualNetwork.getBandwidth(j, n)

            for c in candidates[j]:
                costs, _ = physicalNetwork.dijkstra(c, bandwidth)

                neighbourCandidatesCosts = map(
                    lambda nc: beta * costs[nc] if nc in mapping.values()
                        else costs[nc],
                    candidates[n]
                )

                if c in pi.keys():
                    pi[c] = (pi[c] + min(neighbourCandidatesCosts)) / 2 
                else:
                    pi[c] = min(neighbourCandidatesCosts)

        pi = list(map(lambda item:
            (item[0], physicalNetwork.getNodeStress(item[0]) * item[1]),
            pi.items()))

        pi = list(filter(lambda x: x[0] not in mapping.values(), pi))
        pi.sort(key=lambda x: x[1])
        mapping[j] = pi[0][0]

    linkMapping = dict()
    for j in range(nv):
        neighbours = list(filter(
            lambda x: x > j,
            virtualNetwork.getNeighbours(j)
        ))
        v = mapping[j]

        for n in neighbours:
            bandwidth = virtualNetwork.getBandwidth(j, n)
            u = mapping[n]
            _, paths = physicalNetwork.dijkstra(v, bandwidth)
            path = paths[u]

            for link in path:
                linkMapping[(j, n)] = link

    print('Nodes mapping: virtual node -> physical node') 
    print(mapping)
    print('Link mapping: virtual link -> physical link') 
    print(linkMapping)

    print('Cost function value: ', cf.costFunction(mapping, linkMapping, physicalNetwork, virtualNetwork))

algorithm(data.physicalNetwork, data.virtualNetwork)