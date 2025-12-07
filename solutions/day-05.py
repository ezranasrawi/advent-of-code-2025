from _getinput import getinput

data = getinput('05', True)

ranges, nums = [], []

for line in data:
    if line == '':
        continue
    if '-' in line:
        start, end = line.split('-')
        ranges.append((int(start), int(end)))
    else:
        nums.append(int(line))

fresh = 0

for num in nums:
    for start, end in ranges:
        if start <= num <= end:
            fresh += 1
            break
    
print(f"Part 1: {fresh}")

print(ranges)
