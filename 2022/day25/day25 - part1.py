file = open("input.txt")
lines = file.read().splitlines()


decode = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}

encode = {v: k for k, v in decode.items()}


def snafu2int(number):
    res = 0
    for i, n in enumerate(reversed(number)):
        res += decode[n] * (5**i)

    return res


def int2snafu(number):
    if number == 0:
        return ""

    r = (number + 2) % 5 - 2
    q = (number + 2) // 5

    return int2snafu(q) + encode[r]


res = 0
for number in lines:
    res += snafu2int(number)

print(int2snafu(res))
