from functools import cache


file = open("input.txt")

lines = file.read().splitlines()

cwd = []
cur_dir_content = []
files = {}
folders = set()
folders.add("/")
for line in lines:
    if line.startswith("$"):
        if len(cur_dir_content) != 0:
            files["/".join(cwd)] = cur_dir_content.copy()
            cur_dir_content = []
        if line[2:4] == "cd":
            dir = line.split()[-1]
            match dir:
                case "/":
                    cwd = ["/"]
                case "..":
                    cwd.pop()
                case _:
                    cwd.append(dir)
    else: # listing
        size, name = line.split()
        if size == "dir":
            size = -1
            name = "/".join(cwd + [name])
            folders.add(name)
        cur_dir_content.append((name, int(size)))

if len(cur_dir_content) != 0:
    files["/".join(cwd)] = cur_dir_content.copy()
    cur_dir_content = []


@cache
def get_size(dir):
    total_size = 0
    for file, size in files[dir]:
        if size == -1:
            size = get_size(file)
        total_size += size
    return total_size

needed_size = 30000000 - (70000000 - get_size("/"))
fitting_size = []
for folder in folders:
    size = get_size(folder)
    if size >= needed_size:
        fitting_size.append(size)

fitting_size.sort()
print(fitting_size[0])
