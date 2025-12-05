a, b = 11, 22

a = 1188511880
b =1188511890

numbers = list(range(a,b+1))

def eval_number(num):
    s = str(num)
    mid = len(s) // 2

    return s[:mid] == s[mid:]

from _getinput import getinput

data = getinput('02', False)

def parse_input(data):

    pairs = []
    for part in data.split(","):
        a, b = part.split("-")
        pairs.append((int(a), int(b)))
    
    return pairs

pairs = parse_input(data)

total = 0
for pair in pairs:
    a, b = pair
    for num in range(a, b + 1):
        if eval_number(num):
            total+=num

print(f"Total invalid: {total}")


