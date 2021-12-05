file = open("input.txt")
numbers = list(map(int, file.readlines()))

res = 0
last = None
for i, n in enumerate(numbers[:-2]):
    s = sum(numbers[i:][:3])
    if last is not None:
        if s > last: res += 1
    last = s

print(res)