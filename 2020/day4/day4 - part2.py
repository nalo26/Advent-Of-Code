file = open("input.txt")

lines = []
tmp = {}
for inp in file.readlines():
    line = inp.replace('\n', '')
    if line == "":
        lines.append(tmp)
        tmp = {}
        continue
    for attr in line.split(' '):
        k, v = attr.split(":")
        tmp[k] = v
lines.append(tmp)

def diff(li1, li2):
    return list(set(li1)-set(li2))

def areNbAndLtrs(word):
    for l in word:
        if l.lower() not in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            return False
    return True


neededKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #, 'cid']

invalid = 0
for i, passport in enumerate(lines):
    dif = diff(neededKeys, list(passport.keys()))
    if len(dif) > 0:
        invalid += 1
        print("Invalid amount of info for", i, "(missing", dif, ")")
        continue
    try:
        if len(passport['byr']) != 4 or not(1920 <= int(passport['byr']) <= 2002):
            invalid += 1
            print("Invalid byr for", i)
            continue
        if len(passport['iyr']) != 4 or not(2010 <= int(passport['iyr']) <= 2020):
            invalid += 1
            print("Invalid iyr for", i)
            continue
        if len(passport['eyr']) != 4 or not(2020 <= int(passport['eyr']) <= 2030):
            invalid += 1
            print("Invalid eyr for", i)
            continue
        if (passport['hgt'][-2:] == "cm" and not(150 <= int(passport['hgt'][:-2]) <= 193)) or \
           (passport['hgt'][-2:] == "in" and not(59  <= int(passport['hgt'][:-2]) <= 76 )):
            invalid += 1
            print("Invalid hgt for", i)
            continue
        if passport['hcl'][0] != '#' or len(passport['hcl'][1:]) != 6 or not(areNbAndLtrs(passport['hcl'][1:])):
            invalid += 1
            print("Invalid hcl for", i)
            continue
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            invalid += 1
            print("Invalid ecl for", i)
            continue
        if len(passport['pid']) != 9 or int(passport['pid']) == -1:
            invalid += 1
            print("Invalid pid for", i)
            continue            
    except Exception:
        invalid += 1
        print("Invalid format for", i)
        

print(len(lines) - invalid)