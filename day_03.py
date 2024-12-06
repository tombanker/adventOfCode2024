import re

filename = 'day_03.txt'
with open(filename) as f:
    message = f.read()

# message = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

def part_one():
    pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
    matches = re.findall(pattern, message)
    total = sum([int(i) * int(j) for i,j in matches])
    return total


# message = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
pattern = r"do(?:n't)?|mul\((?:[0-9]{1,3}),(?:[0-9]{1,3})\)"


matches = re.findall(pattern, message)
sign = 1

total = 0
for match in matches:
    if match == "don't":
        sign = 0
    elif match == "do":
        sign = 1
    else:
        pattern = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
        match = re.findall(pattern, match)[0]
        total += sign * int(match[0]) * int(match[1])

print(total)