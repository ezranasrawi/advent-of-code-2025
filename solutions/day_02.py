#--- Day 2: Gift Shop ---

from _getinput import getinput

def parse_input(data):
    pairs = []
    for part in data.split(","):
        a, b = part.split("-")
        pairs.append((int(a), int(b)))
    
    return pairs

def is_split(num):
    s = str(num)
    mid = len(s) // 2

    return s[:mid] == s[mid:]

def is_repeating(s: str) -> bool:
    return s in (s + s)[1:-1]

data = getinput('02', False)
pairs = parse_input(data)

part1, part2 = 0, 0

for pair in pairs:
    a, b = pair
    for num in range(a, b + 1):
        if is_split(num):
            part1 += num
        if is_repeating(str(num)):
            part2 += num

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")