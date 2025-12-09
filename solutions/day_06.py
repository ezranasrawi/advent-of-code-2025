from _getinput import getinput

data = getinput('06', True)

data = [line.split() for line in data]
data = list(map(list, zip(*data)))

total = 0

for line in data:
    op = line.pop(-1) 
    total += eval(op.join(line))

print(total)

