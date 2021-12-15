file = open("input.txt")

caves = {}
def seek(node, visited = set()):
    if node == 'end': return 1
    count = 0
    for next in caves[node]:
        if next in visited: continue
        count += seek(next, visited | {node} if node == node.lower() else visited)
    return count


for line in file.readlines():
    s, e = line.replace("\n", "").split("-")
    caves.setdefault(s, []).append(e)
    caves.setdefault(e, []).append(s)

print(seek('start'))