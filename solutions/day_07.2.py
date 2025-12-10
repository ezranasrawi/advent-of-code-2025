from _getinput import getinput

data = getinput('07', False)

sy, sx = 0, data[0].find('S')

queue = [(sy, sx)]
timelines = {(sy, sx): 1}
dy = 1

def update_timelines(ny, nx, timelines, count):
    if (ny, nx) not in timelines:
        timelines[(ny, nx)] = count
        queue.append((ny, nx))
    else:
        timelines[(ny, nx)] += count

answer = 0

while queue:

    sy, sx = queue.pop(0)
    count = timelines[(sy, sx)]

    ny, nx = sy + dy, sx

    if ny > len(data) - 1:
        answer += count
        continue

    next = data[ny][nx]

    if next == '.':
        update_timelines(ny, nx, timelines, count)
        continue

    if next == '^':
        ly, lx = ny, nx - 1
        update_timelines(ly, lx, timelines, count)

        ry, rx = ny, nx + 1
        update_timelines(ry, rx, timelines, count)

        continue

print("Part 2:", answer)
