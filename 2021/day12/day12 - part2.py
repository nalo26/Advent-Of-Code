file = open("input.txt")

caves = {}
def seek(node, visited = set(), doubled = False):
    if node == 'end': return 1
    count = 0
    for next in caves[node]:
        if 'start' == next: continue
        if next in visited and doubled: continue
        if next in visited: 
            count += seek(next, visited | {node} if node == node.lower() else visited, True)
        else:
            count += seek(next, visited | {node} if node == node.lower() else visited, doubled)
    return count


for line in file.readlines():
    s, e = line.replace("\n", "").split("-")
    caves.setdefault(s, []).append(e)
    caves.setdefault(e, []).append(s)

print(seek('start'))