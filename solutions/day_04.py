from _getinput import getinput

data = getinput('04', False)
dirs = ((-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1))

def out_of_bounds(x,y):
    return not (0 <= x < len(data) and 0 <= y < len(data[0]))

def adjacent(x, y):
    for dx, dy in dirs:
        if not out_of_bounds(x + dx, y + dy):
            yield (x + dx, y + dy)

grand_total = 0
tries = 0

while True:
    total = 0
    tries += 1
    updates = []

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '@':
                
                adj = list(adjacent(x, y))
                count = 0

                for ax, ay in adj:
                    if data[ay][ax] == '@':
                        count += 1
                if count < 4:
                    total += 1
                    updates.append((x, y))

    for x, y in updates:
        data[y] = data[y][:x] + '.' + data[y][x+1:]

    if tries == 1:
        print(f"Part 1: {total}")

    grand_total += total

    if total == 0:
        break

print(f"Part 2: {grand_total}")