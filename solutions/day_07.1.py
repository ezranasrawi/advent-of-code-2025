from _getinput import getinput

data = getinput('07', False)

sy, sx = 0, data[0].find('S')

queue = [(sy, sx)]
visited = set()
dy = 1
splits = 0

while queue: 

    sy, sx = queue.pop(0)
    ny, nx = sy + dy, sx

    if ny > len(data) - 1:
        continue

    next = data[ny][nx]

    if (ny, nx) in visited:
        continue

    if next == '.':
        queue.append((ny, nx))
        visited.add((ny, nx))
        continue

    if next == '^':
        visited.add((ny, nx))
        left = [ny, nx - 1]
        right = [ny, nx + 1]

        queue.append(left)
        queue.append(right)

        splits += 1

print('Part 1', splits)