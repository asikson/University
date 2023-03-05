from dataLink10 import *
import random

# for minYk in minYks:
#     print(minYk)
#     pn.algorithm(m, x0, w, minYk, utilityFunctions)

sumCost, sumUsage, sumCongestion = 0, 0, 0

tests = 10

for _ in range(tests):
    x0 = []
    
    for i in mRange:
        tmp = [random.randint(100, 500) for _ in nRange]
        tmp = tmp * 2
        x0.append(tmp)

    cost, usage, congestion = pn.algorithm(m, x0, w, minYks[1], utilityFunctions)
    sumCost += cost
    sumUsage += usage
    sumCongestion += congestion

sumCost = round(sumCost / tests, 3)
sumUsage = round(sumUsage / tests, 2)
sumCongestion = round(sumCongestion / tests, 2)

print('Wypłata: ', sumCost)
print('Użycie łączy fiz: ', sumUsage)
print('Przeciążenie: ', sumCongestion)
print('\n')