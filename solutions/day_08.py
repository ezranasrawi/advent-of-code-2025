from _getinput import getinput
import math

def euclidean(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt(
        (x1 - x2)**2 +
        (y1 - y2)**2 +
        (z1 - z2)**2
    )

data = getinput('08', example=True)

data = [line.split(',') for line in data]
data = [tuple(map(int, line)) for line in data]

pairs = []
for i, p1 in enumerate(data):
    for j, p2 in enumerate(data):
        if i < j:
            distance = euclidean(p1, p2)
            pairs.append((distance, i, j))

pairs.sort()
print(pairs)
