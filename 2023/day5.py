from threading import Thread

from tqdm import tqdm

file = open("input.txt")
content = file.read().split("\n\n")
seeds = list(map(int, content.pop(0).split(": ")[1].split()))
mapping = []

for cont in content:
    cont = cont.split("\n")
    new_map = set()
    for _map in cont[1:]:
        # destination start, source start, range length
        ds, ss, rl = tuple(map(int, _map.split()))
        new_map.add(((ds, ds + rl), (ss, ss + rl)))
    mapping.append(new_map)

threads = [None] * (len(seeds) // 2)
results = [None] * (len(seeds) // 2)


def get_location(value: int) -> int:
    current_value = value
    for _map in mapping:
        for _match in _map:
            m = _match[1]
            if m[0] <= current_value < m[1]:
                offset = current_value - _match[1][0]
                current_value = _match[0][0] + offset
                break
    return current_value


def part1():
    locations = []
    for seed in seeds:
        locations.append(get_location(seed))
    return min(locations)


def thread_part2(seed_range, index):
    _min = None
    for seed in tqdm(seed_range):
        location = get_location(seed)
        if _min is None or location < _min:
            _min = location
    results[index] = _min


def part2():
    for i in range(0, len(seeds), 2):
        seed_range = range(seeds[i], seeds[i] + seeds[i + 1])
        t = Thread(target=thread_part2, args=(seed_range, i // 2))
        t.start()
        threads[i // 2] = t

    for t in threads:
        t.join()

    return min(results)


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
