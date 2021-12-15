file = open("input.txt")
lines = file.readlines()

template = lines[0].replace("\n", "")
occurences = {}

for x, y in zip(template, template[1:]):
    if x + y not in occurences: occurences[x+y] = 0
    occurences[x+y] += 1

rules = {}
for rule in lines[2:]:
    pair, elem = rule.replace("\n", "").split(" -> ")
    rules[pair] = elem

for _ in range(40):
    newOccurences = {}
    for pair in occurences:
        rule = rules[pair]
        if pair[0]+rule not in newOccurences: newOccurences[pair[0]+rule] = 0
        newOccurences[pair[0]+rule] += occurences[pair]
        if rule+pair[1] not in newOccurences: newOccurences[rule+pair[1]] = 0
        newOccurences[rule+pair[1]] += occurences[pair]
    occurences = newOccurences

first_letter = {}
secnd_letter = {}
for pair in occurences:
    if pair[0] not in first_letter: first_letter[pair[0]] = 0
    first_letter[pair[0]] += occurences[pair]
    if pair[1] not in secnd_letter: secnd_letter[pair[1]] = 0
    secnd_letter[pair[1]] += occurences[pair]

_count = {x: max(first_letter.get(x, 0), secnd_letter.get(x, 0)) for x in set(first_letter) | set(secnd_letter)}
print(max(_count.values()) - min(_count.values()))