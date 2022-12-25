import re


class Robot:
    def mine(self, ore=False, clay=False, obsidian=False, geode=False) -> tuple[int]:
        return int(ore), int(clay), int(obsidian), int(geode)


class OreRobot(Robot):
    def mine(self):
        return super().mine(ore=True)


class ClayRobot(Robot):
    def mine(self):
        return super().mine(clay=True)


class ObsiRobot(Robot):
    def mine(self):
        return super().mine(obsidian=True)


class GeodeRobot(Robot):
    def mine(self):
        return super().mine(geode=True)


file = open("input.txt")
lines = file.read().splitlines()

for line in lines:
    match = re.findall("\d+", line)
    costs = tuple(map(int, match))
    ores, clays, obsi, geodes = 0, 0, 0, 0
    robots = {OreRobot()}
    for _ in range(24):
        new_robots = set()
        if ores >= costs[5] and obsi >= costs[6]:
            ores -= costs[5]
            obsi -= costs[6]
            new_robots.add(GeodeRobot())
        if ores >= costs[3] and clays >= costs[4]:
            ores -= costs[5]
            clays -= costs[4]
            new_robots.add(ObsiRobot())
        if ores >= costs[2]:
            ores -= costs[2]
            new_robots.add(ClayRobot())
        if ores >= costs[1]:
            ores -= costs[1]
            new_robots.add(OreRobot())

        for robot in robots:
            ore, clay, ob, geode = robot.mine()
            ores += ore
            clays += clay
            obsi += ob
            geodes += geodes

        robots |= new_robots

    print(geodes)
