from math import exp, log10
import random
from physical_network import PhysicalNetwork

# liczba linków fizycznych
n = 10
nRange = range(0, n)

def nRangeWithout(k):
    return list(range(0, k - 1)) + list(range(k, n))

# liczba linków wirtualnych
m = 2
mRange = range(0, m)

# przepustowości linków sieci fizycznej
c = [100, 900, 400, 500, 100, 500, 900, 300, 500, 600]

# ceny za użycie linków fizycznych
P = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]

# kary za przeciążenie linków fizycznych
B = [0.1, 0.08, 0.1, 0.2, 0.1, 0.3, 0.03, 0.15, 0.4, 0.1]

# wagi cen linków dla sieci wirtualnych
w = [
    [1, 10, 1, 10, 1, 10, 1, 10, 1, 10],
    [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]
]

# początkowe wartości wektorów x dla sieci wirtualnych
x0 = []
for i in mRange:
    tmp = []
    for j in nRange:
        tmp.append(random.randint(100, 500))
    tmp = tmp * 2
    x0.append(tmp)
print("x0:", x0)
l0 = 1
l = [10, 15]
q = 0.5

# przykładowe funkcje użyteczności
def end2endDelay(yk, zk):
    result = 0
    for j in range(0, n):
        if (yk[j] > 0):
            try:
                e = exp(zk[j] / yk[j])
                product = zk[j] * (l[j] + l0 * e)
                result += product
            except:
                pass

    return -1 * result

def logarithmicPathRate(yk, zk):
    result = 0
    for j in nRange:
        if (yk[j] > 0):
            try:
                left = log10(zk[j])
                right = q * exp(zk[j] / yk[j])
                result += left - right
            except:
                pass

    return result

# tablica funkcji użyteczności
utilityFunctions = [
    logarithmicPathRate,
    logarithmicPathRate
]

minYks = [
    [400, 400],
    [500, 500],
    [600, 600],
    [700, 700],
    [800, 800]
]

pn = PhysicalNetwork(n, c, P, B)