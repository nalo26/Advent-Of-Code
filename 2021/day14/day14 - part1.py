file = open("input.txt")
lines = file.readlines()

template = lines[0].replace("\n", "")

rules = {}
for rule in lines[2:]:
    pair, elem = rule.replace("\n", "").split(" -> ")
    rules[pair] = elem

for _ in range(10):
    newTemplate = template[0]
    for poly in template[1:]:
        newTemplate += rules[newTemplate[-1] + poly]
        newTemplate += poly
    template = newTemplate

most_common = template.count(max(set(template), key=template.count))
least_common = template.count(min(set(template), key=template.count))
print(most_common - least_common)
