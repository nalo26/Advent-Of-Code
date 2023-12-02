from hashlib import md5

key = open("input.txt").readline()

answer = 0
while True:
    to_code = key + str(answer)
    hash = md5(to_code.encode()).hexdigest()
    if hash.startswith("00000"):
        break
    answer += 1

print(answer)
