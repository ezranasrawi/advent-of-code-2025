from _getinput import getinput

data = getinput('05', False)

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

sorted_ranges = sorted(ranges)
merged_ranges = []

for start, end in sorted_ranges:
    if not merged_ranges or merged_ranges[-1][1] < start:
        merged_ranges.append((start, end))
    else:
        s, e = merged_ranges[-1]
        merged_ranges[-1] = (s, max(e, end))

total_covered = 0
for start, end in merged_ranges:
    total_covered += end - start + 1

print(f"Part 2: {total_covered}")