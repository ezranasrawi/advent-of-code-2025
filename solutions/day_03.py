# --- Day 3: Lobby ---

from _getinput import getinput

data = getinput('03', False)

def find_highest(line, max_items):

    number = ''
    start = 0

    for i in range(max_items):
        remaining = max_items - i
        end = len(line) - remaining + 1

        max_digit = max(line[start:end])
        number += max_digit

        start = line.find(max_digit, start) + 1

    return int(number)

total = 0
for line in data:
    max_items = 2
    highest = find_highest(line, max_items)
    total += highest

print(f"Part 1: {total}")

total = 0
for line in data:
    max_items = 12
    highest = find_highest(line, max_items)
    total += highest    

print(f"Part 2: {total}")