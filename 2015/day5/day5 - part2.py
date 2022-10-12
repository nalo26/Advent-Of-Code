import os
import re


def path(path, file):
    return os.sep.join(os.path.abspath(path).split(os.sep)[:-1] + [file])


file = open(path(__file__, "input.txt"))
lines = file.readlines()


nice = 0
for line in lines:
    line = line.replace("\n", "")

    if re.search(r"(..).*\1", line) is None:
        continue

    match = re.findall(r"(.)(.)\1", line)
    if len(match) == 0:
        continue
    for m in match:
        if m[0] != m[1]:
            break
    else:
        continue

    # print(line)
    nice += 1

print(nice)
