from scipy.optimize import minimize
from constraints import getAdditionalConstraintForVN, getAdditionalConstraints, getConstraints, getConstraintsForVN
from utils import getEmptyX, getYFromX, getZ, getZFromX, rangeWithout, getY


class PhysicalNetwork:

    def __init__(self, n, c, P, B):
        self.n = n
        self.nRange = range(0, n)
        self.c = c
        self.P = P
        self.B = B

    def usage(self, y):
        result = [0 for _ in self.nRange]

        for yk in y:
            for i in self.nRange:
                result[i] += yk[i]

        for i in self.nRange:
            result[i] = min(result[i], self.c[i])
        
        return sum(result) / sum(self.c)

    def congestion(self, y):
        result = [0 for _ in self.nRange]
        for yk in y:
            for i in self.nRange:
                result[i] += yk[i]
        result = [result[idx] if result[idx] >= self.c[idx] else 0 for idx, _ in enumerate(result)]
        return round(sum(result) / sum(self.c), 2)

    def pricingFunction(self, k, yk, w):
        product = [self.P[j] * w[k][j] * yk[j] for j in self.nRange]
        return sum(product)

    def congestionFunction(self, k, yk, z, m):
        result = 0

        for j in self.nRange:
            fact = self.B[j] * yk[j]
            up = sum(z[i][j] for i in rangeWithout(m, k))
            left = up / self.c[j] - 1
            result += fact * left
    
        return result

    def costFunction(self, xk, k, z, w, utilityFunctions, m):
        yk = xk[0 : self.n]
        zk = xk[self.n : (2 * self.n)]
        U = utilityFunctions[k](yk, zk)

        price = self.pricingFunction(k, yk, w)
        congestion = self.congestionFunction(k, yk, z, m)

        result = U - price - congestion 
        return round(-1 * result, 4)

    def sumCostFunction(self, x, m, w, utilityFunctions):
        result = 0
        z = getZFromX(x, m, self.n)

        for k in range(0, m):
            yk = x[2*k * self.n : 2*(k+1) * self.n]
            xk = yk[0: self.n]
            
            cost = self.costFunction(xk, k, z, w, utilityFunctions, m)
            result += cost

        return result

    def getBoundsForVN(self):
        return [(0, self.c[i]) for i in self.nRange] * 2

    def getAllBounds(self, m):
        return self.getBoundsForVN() * m

    def getConstraintsForVN(self, minYk):
        return getConstraintsForVN + getAdditionalConstraintForVN(minYk)

    def getAllConstraints(self, minYks):
        return getConstraints + getAdditionalConstraints(minYks)

    def solveForVN(self, k, xk, z, w, minYks, utilityFunctions, m):
        bnds = self.getBoundsForVN()
        const = self.getConstraintsForVN(minYks[k])
        solution = minimize(self.costFunction, xk, args=(k, z, w, utilityFunctions, m), bounds=bnds, constraints=const)
        return list(map(lambda x: round(x, 2), solution.x))

    def isAdditionalConstraintViolated(self, xk, minYk):
        return sum(xk[0 : self.n]) < minYk

    def algorithm(self, m, x0, w, minYks, utilityFunctions):

        x = getEmptyX(self.n, m)
        costs = [0 for _ in range(0, m)]
        z = [getZ(xk, self.n) for xk in x0]
        newX = x0
        changed = m

        while changed > 0:
            changed = 0
            x = newX
            z = [getZ(xk, self.n) for xk in newX]

            for k in range(0, m):
                newXK = self.solveForVN(k, x[k], z, w, minYks, utilityFunctions, m)
                costs[k] = self.costFunction(x[k], k, z, w, utilityFunctions, m)
                newCost = self.costFunction(newXK, k, z, w, utilityFunctions, m)
                if newCost <  costs[k] \
                    or self.isAdditionalConstraintViolated(x[k], minYks[k]):

                    changed += 1
                    newX[k] = newXK
                    costs[k] = newCost

        sumCost = sum(costs)
        y = [getY(xk, self.n) for xk in newX]

        # print(newX)

        return round(-1 * sumCost, 3), self.usage(y), self.congestion(y)


    def solver(self, m, x0, w, minYks, utilityFunctions):
        bnds = self.getAllBounds(m)
        const = self.getAllConstraints(minYks)
        solution = minimize(self.sumCostFunction, x0, args=(m, w, utilityFunctions), bounds=bnds, constraints=const)

        y = getYFromX(solution.x, m, self.n)

        # print(solution.x)

        return round(-1 * solution.fun, 3), self.usage(y), self.congestion(y)