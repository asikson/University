import nodes as data
from pyscipopt import Model, quicksum

epsilon = 1e-100
model = Model()

def solver(np, nv,
    physicalNodes, physicalCapacities,
    virtualNodes, virtualCapacities
):

    # ZMIENNE DECYZYJNE
    x = [[model.addVar(vtype="B", name=f"x[{m}][{i}]")
            for i in range(np)]
                for m in range(nv)]
    y = [[[[model.addVar(vtype="B", name=f"y[{m}][{n}][{i}][{j}]")
        for j in range(np)]
            for i in range(np)]
                for n in range(nv)]
                    for m in range(nv)]

    # zmienne optymalizacyjne
    CMaxLoad = model.addVar(vtype="C", name="CMaxLoad")
    MMaxLoad = model.addVar(vtype="C", name="MMaxLoad")
    BMaxLoad = model.addVar(vtype="C", name="BMaxLoad")


    # OGRANICZENIA
    #maxLoads
    for i, pn in enumerate(physicalNodes):
        virtualLoads = [x[m][i] * vn.C for m, vn in enumerate(virtualNodes)]
        model.addCons(
            pn.F * quicksum(virtualLoads) / pn.C <= CMaxLoad,
            f"CMaxLoad({i})"
        )

    for i, pn in enumerate(physicalNodes):
        virtualLoads = [x[m][i] * vn.M for m, vn in enumerate(virtualNodes)]
        model.addCons(
            pn.F * quicksum(virtualLoads) / pn.M <= MMaxLoad,
            f"MMaxLoad({i})"
        )

    for j in range(np):
        for i in range(j):
            if (physicalCapacities[i][j] > 0):
                virtualLoads = [y[m][n][i][j] * virtualCapacities[m][n]
                    for m in range(nv) for n in range(nv)]
                model.addCons(
                    quicksum(virtualLoads) / physicalCapacities[i][j] <= BMaxLoad,
                    f"BMaxLoad({i}, {j})"
                )

    # przypisanie węzłów
    for m in range(nv):
        model.addCons(
            quicksum([x[m][i] for i in range(np)]) == 1,
            f"VirtualNodesConservation({m})"
        )

    for i in range(np):
        model.addCons(
            quicksum([x[m][i] for m in range(nv)]) <= 1,
            f"PhysicalNodesConservation({i})"
        )

    # ochrona procesora
    for i, pn in enumerate(physicalNodes):
        model.addCons(
            quicksum([x[m][i] * vn.C for m, vn in enumerate(virtualNodes)]) <= pn.C,
            f"CPUConservation({i})"
        )

    # ochrona pamięci
    for i, pn in enumerate(physicalNodes):
        model.addCons(
            quicksum([x[m][i] * vn.M for m, vn in enumerate(virtualNodes)]) <= pn.M,
            f"MemoryConservation({i})"
        )

    # ochrona częstotliwości
    for i, pn in enumerate(physicalNodes):
        model.addCons(
            quicksum([x[m][i] * vn.F for m, vn in enumerate(virtualNodes)]) <= pn.F,
            f"FrequencyConservation({i})"
        )

    # ochrona przepływów
    for n in range(nv):
        for m in range(n):
            for i in range(np):
                diffs = [y[m][n][i][j] - y[m][n][j][i] for j in range(np)]
                model.addCons(
                    quicksum(diffs) == x[m][i] - x[n][i],
                    f"Node-link({i})"
                )

    # ochrona przepustowości
    for j in range(np):
        for i in range(j):
            capacityLoads = [virtualCapacities[m][n] * (y[m][n][i][j] + y[m][n][j][i])
                for n in range(nv) for m in range(n)]
            model.addCons(
                quicksum(capacityLoads) <= physicalCapacities[i][j],
                f"CapacityConservation({i},{j})"
            )

    #FUNKCJA KOSZTU
    linkUsage = quicksum([y[m][n][i][j] * virtualCapacities[m][n]
        for n in range(nv) for m in range(n) for i in range(np) for j in range(np)])

    costFunction = CMaxLoad + MMaxLoad + BMaxLoad + epsilon * linkUsage

    model.setObjective(costFunction, "minimize")
    model.optimize()

    return model

solver(data.np, data.nv,
    data.physicalNodes, data.physicalCapacities,
    data.virtualNodes, data.virtualCapacities).printBestSol()