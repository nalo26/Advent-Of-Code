file = open("input.txt").read()
blocks = file.split("\n\n")

fields = {}
for line in blocks[0].split("\n"):
    line = line.replace(": ", "'] = [[")
    line = line.replace(" or ", "], [")
    line = line.replace("-", ", ")
    line = "fields['" + line
    line += "]]"
    exec(line)

myTicket = blocks[1].split("\n")[1].split(",")
nearbyTickets = [list(map(int, ticket.split(","))) for ticket in blocks[2].split("\n")[1:]]

def isValid(v, fields):
    for field in fields.values():
        for param in field:
            if param[0] <= v <= param[1]: return True
    return False


res = 0
for ticket in nearbyTickets:
    for v in ticket:
        if not isValid(v, fields): res += v
print(res)