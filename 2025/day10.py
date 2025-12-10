from z3 import Int, Optimize, sat

from lib.input import get_input

lines = get_input(2025, 10).splitlines()
lights, buttons, joltages = [], [], []
for line in lines:
    line = line.split()
    lights.append(tuple(map(lambda x: int(x == "#"), line[0][1:-1])))
    buttons.append([tuple(map(int, b.strip("()").split(","))) for b in line[1:-1]])
    joltages.append(tuple(map(int, line[-1].strip("{}").split(","))))


def solve(targets: tuple[int], buttons: list[tuple[int]], p2=False):
    opt = Optimize()
    button_vars = []  # How many times each button should be pressed
    for i in range(len(buttons)):
        b = Int(f"button_{i}")  # Integer number of presses
        button_vars.append(b)
        opt.add(b >= 0)  # Positive number of presses

    # Constraints for each light
    for i, light in enumerate(targets):
        affecting_buttons = [button_vars[j] for j, btn_list in enumerate(buttons) if i in btn_list]

        if affecting_buttons:
            s = sum(affecting_buttons)
            if p2:
                opt.add(s == light)  # Exact number of presses to reach the target joltage
            else:  # p1
                opt.add(s % 2 == light)  # Pressing 2 times is the same as not pressing

    # Minimizing total button presses
    total = sum(button_vars)
    opt.minimize(total)

    if opt.check() == sat:
        model = opt.model()
        result_buttons = [model[b].as_long() for b in button_vars]  # Total presses for each button
        return sum(result_buttons)
    raise ValueError("No solution")


def part1():
    return sum(solve(light, button) for light, button in zip(lights, buttons))


def part2():
    return sum(solve(joltage, button, True) for joltage, button in zip(joltages, buttons))
