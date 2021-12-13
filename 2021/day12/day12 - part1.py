file = open("input.txt")

caves = {}
def seek(start, visited):
    if start == 'end': return 1
    if len(caves[start]) == 1 and caves[start][0].lower() == caves[start][0]: return 0
    if start in visited: return 0
    if start.lower() == start: visited.append(start)
    count = 0
    for path in caves[start]:
        count += seek(path, visited.copy())
    return count


for line in file.readlines():
    s, e = line.replace("\n", "").split("-")
    caves.setdefault(s, []).append(e)
    caves.setdefault(e, []).append(s)
    
print(seek('start', []))