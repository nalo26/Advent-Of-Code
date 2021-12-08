from typing import MutableMapping


file = open("input.txt")
fuels = list(map(int, file.readline().split(",")))

min_cost = -1
for i in range(max(fuels)):
    cost = 0
    for fuel in fuels:
        cost += abs(fuel - i)
    if min_cost == -1 or cost < min_cost:
        min_cost = cost

print(min_cost)