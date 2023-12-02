import itertools
from functools import cache

file = open("input.txt")

p1 = int(file.readline().split(": ")[1])
p2 = int(file.readline().split(": ")[1])

WIN_SCORE = 21


@cache
def play(p1, p2, p1_score=0, p2_score=0):
    win_amount = [0, 0]
    for roll1 in itertools.product([1, 2, 3], repeat=3):
        for roll2 in itertools.product([1, 2, 3], repeat=3):
            _p1 = (sum(roll1) + p1 - 1) % 10 + 1
            _p2 = (sum(roll2) + p2 - 1) % 10 + 1
            _p1_score = p1_score + _p1
            _p2_score = p2_score + _p2

            if _p1_score >= WIN_SCORE:
                win_amount[0] += 1
                break
            if _p2_score >= WIN_SCORE:
                win_amount[1] += 1
                continue

            step = play(_p1, _p2, _p1_score, _p2_score)
            win_amount[0] += step[0]
            win_amount[1] += step[1]
    return win_amount


print(max(play(p1, p2)))
