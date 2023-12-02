file = open("input.txt")


class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0


p1 = Player(int(file.readline().split(": ")[1]))
p2 = Player(int(file.readline().split(": ")[1]))

players = [p1, p2]
p_index = 0
dice = 0
while p1.score < 1000 and p2.score < 1000:
    index = p_index % 2
    score = 0
    for _ in range(3):
        dice += 1
        score += (dice - 1) % 100 + 1
    players[index].position += score
    players[index].position = (players[index].position - 1) % 10 + 1
    players[index].score += players[index].position
    p_index += 1

if p1.score >= 1000:
    print(p2.score * dice)
else:
    print(p1.score * dice)
