import regex as re  # overlapping does not exists in re module

file = open("input.txt")
lines = file.readlines()


def part1():
    num_re = re.compile(r"\d")
    _sum = 0
    for instruction in lines:
        nums = num_re.findall(instruction)
        _sum += int(nums[0] + nums[-1])
    return _sum


def part2():
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    num_re = re.compile(r"\d|" + r"|".join(numbers.keys()))
    _sum = 0
    for instruction in lines:
        nums = num_re.findall(instruction, overlapped=True)  # overlapped is the key (eighthree = 83)
        _sum += int(numbers.get(nums[0], nums[0]) + numbers.get(nums[-1], nums[-1]))
    return _sum


print("Part 1:", part1())
print("Part 2:", part2())
file.close()
