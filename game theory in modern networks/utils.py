def getEmptyX(n, m):
    return [ [0 for _ in range(0, n)] * 2 for _ in range(0, m)]

def rangeWithout(n, k):
    return list(range(0, k - 1)) + list(range(k, n))

def getZ(xk, n):
    return xk[n : 2 * n]

def getZFromX(x, m, n):
    result = []
    for k in range(0, m):
        offset = 2 * k * n
        xk = x[offset : offset + 2 * n]
        result.append(getZ(xk, n))

    return result

def getY(xk, n):
    return xk[0 : n]

def getYFromX(x, m, n):
    result = []
    for k in range(0, m):
        offset = 2 * k * n
        xk = x[offset : offset + 2 * n]
        result.append(getY(xk, n))

    return result
