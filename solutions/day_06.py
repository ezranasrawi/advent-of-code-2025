from _getinput import getinput

data = getinput('06', False)

data = [line.split() for line in data]
data = list(map(list, zip(*data)))
ops, nums = [], []

for i, line in enumerate(data):
    ops.append(line.pop(-1))
    nums.append(line)

total = 0

for i, num in enumerate(nums):
    op = ops[i]
    total += eval(op.join(num))

print('Part 1', total)

def parse_r2l(num):
    new = []

    while num:
        last = [n[-1] for n in num]
        num = [n[:-1] for n in num if n[:-1]]
        new.append(''.join(last))

    return new

data = getinput('06', False)
data = list(map(list, zip(*data)))

num = []
total = 0

for line in data:
    line = ''.join(line)
    
    if line[-1] in ['*', '+']:
        op = line[-1]
        n = line[:-1]
        num.append(n.strip())
    
    if line.strip().isdigit():
        n = line.strip()
        num.append(n)

    if line.isspace() or line == data[-1]:
        total += eval(op.join(num))
        num = []

total+= eval(op.join(num))
print('Part 2', total)