from math import exp, log10
from physical_network import PhysicalNetwork

# liczba linków fizycznych
n = 2
nRange = range(0, n)

def nRangeWithout(k):
    return list(range(0, k - 1)) + list(range(k, n))

# liczba linków wirtualnych
m = 2
mRange = range(0, m)

# przepustowości linków sieci fizycznej
c = [100, 900]

# ceny za użycie linków fizycznych
P = [0.01, 0.01]

# kary za przeciążenie linków fizycznych
B = [0.1, 0.08]

# wagi cen linków dla sieci wirtualnych
w = [
    [1, 10],
    [10, 1]
]

# początkowe wartości wektorów x dla sieci wirtualnych
x0 = [
    [130, 470, 130, 470],
    [110, 490, 110, 490]
]

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

pn = PhysicalNetwork(2, c, P, B)