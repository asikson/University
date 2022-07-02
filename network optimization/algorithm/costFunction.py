epsilon = 1e-100

def costFunction(mapping, linkMapping, physicalNetwork, virtualNetwork):
    cpuLoads = list(map(
        lambda m: round(physicalNetwork.getNode(m[1]).F * virtualNetwork.getNode(m[0]).C / physicalNetwork.getNode(m[1]).C, 3,),
        mapping.items()
    ))

    memoryLoads = list(map(
        lambda m: round(physicalNetwork.getNode(m[1]).F * virtualNetwork.getNode(m[0]).M / physicalNetwork.getNode(m[1]).M, 3),
        mapping.items()
    ))

    bandwidths = dict()
    for k, v in linkMapping.items():
        if v not in bandwidths.keys():
            bandwidths[v] = virtualNetwork.getBandwidth(k[0], k[1])
        else:
            bandwidths[v] += virtualNetwork.getBandwidth(k[0], k[1])

    bandwidthLoads = list(map(
        lambda b: round(b[1] / physicalNetwork.getCapacity(b[0][0], b[0][1]), 3),
        bandwidths.items()
    ))

    linkUsage = round(sum(map(
        lambda b: virtualNetwork.getBandwidth(b[0], b[1]),
        linkMapping.keys()
    )), 3)

    return max(cpuLoads) + max(memoryLoads) + max(bandwidthLoads) + epsilon * linkUsage