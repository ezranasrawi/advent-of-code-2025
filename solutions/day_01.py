from _getinput import getinput

data = getinput('01', False)

def count_zeros(data, simulate_steps=False):
    position = 50
    zeros = 0

    for line in data:
        direction = line[0]
        steps = int(line[1:])
        delta = -1 if direction == 'L' else 1

        if simulate_steps:  
            for _ in range(steps):
                position = (position + delta) % 100
                if position == 0:
                    zeros += 1
        else:
            position = (position + delta * steps) % 100
            if position == 0:
                zeros += 1

    return zeros

print('Part 1:', count_zeros(data, simulate_steps=False))
print('Part 2:', count_zeros(data, simulate_steps=True))