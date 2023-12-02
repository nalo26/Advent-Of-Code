# file = open("input.txt")
# lines = file.readlines()

# program = []
# for line in lines:
#     line = line.replace("\n", "").split(" ")
#     match line[0]:
#         case "inp":
#             program.append(f"{line[1]} = model.pop(0)")
#         case "add":
#             if line[2] == "0": continue
#             program.append(f"{line[1]} += {line[2]}")
#         case "mul":
#             if line[2] == "1": continue
#             program.append(f"{line[1]} *= {line[2]}")
#         case "div":
#             if line[2] == "1": continue
#             program.append(f"{line[1]} //= {line[2]}")
#         case "mod":
#             program.append(f"{line[1]} %= {line[2]}")
#         case "eql":
#             program.append(f"{line[1]} = int({line[1]} == {line[2]})")

# for model_number in range(99999999999999, 10000000000000, -1):
#     print(model_number)
#     w, x, y, z = 0, 0, 0, 0
#     model = list(map(int, str(model_number)))
#     for instruction in program:
#         exec(instruction)
#     if z == 0:
#         print(model_number)
#         break

# aborted the above, to long
# let's do maths !
# all credits to https://github.com/dphilipson/advent-of-code-2021/blob/master/src/days/day24.rs

# {CHECK},{OFFSET}
# 11, 6
# 11, 14
# 15, 13
# -14, 1
# 10, 6
# 0, 13
# -6, 6
# 13, 3
# -3, 8
# 13, 14
# 15, 4
# -2, 7
# -9, 15
# -2, 1

# PUSH input[0] + 6
# PUSH input[1] + 14
# PUSH input[2] + 13
# POP. Must have input[3] == popped_value - 14
# PUSH input[4] + 6
# POP. Must have input[5] == popped_value - 0
# POP. Must have input[6] == popped_value - 6
# PUSH input[7] + 3
# POP. Must have input[8] == popped_value - 3
# PUSH input[9] + 14
# PUSH input[10] + 4
# POP. Must have input[11] == popped_value - 2
# POP. Must have input[12] == popped_value - 9
# POP. Must have input[13] == popped_value - 2

# input[3] = input[2] - 14 + 13 (-1)
# input[5] = input[4] - 0 + 6   (+6)
# input[6] = input[1] - 6 + 14  (+8)
# input[8] = input[7] - 3 + 3   (-0)
# input[11] = input[10] - 2 + 4 (+2)
# input[12] = input[9] - 9 + 14 (+5)
# input[13] = input[0] - 2 + 6  (+4)

#   MAX     |    MIN
# 8 = 9 -1  |  1 = 2 -1
# 9 = 3 +6  |  7 = 1 +6
# 9 = 1 +8  |  9 = 1 +8
# 9 = 9 -0  |  1 = 1 -0
# 9 = 7 +2  |  3 = 1 +2
# 9 = 4 +5  |  6 = 1 +5
# 9 = 5 +4  |  5 = 1 +4

# max : 51983999947999
# min : 11211791111365
