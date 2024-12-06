filename = "day_05.txt"
rules, updates = [], []

with open(filename) as f:
    for line in f.readlines():
        line = line.strip()
        if '|' in line:
            i, j = line.split('|')
            rules.append((int(i),int(j)))
        elif ',' in line:
            updates.append([int(i) for i in line.split(',')])

def verify_update(update):
    for i, j in rules:
        if i in update and j in update:
            if update.index(i) > update.index(j):
                return False
    return True

# -------------------------------------------------------------------------------------------------
# part one
# -------------------------------------------------------------------------------------------------
part_one_total = 0
for update in updates:
    if verify_update(update):
        part_one_total += update[len(update)//2]

print(part_one_total)

# -------------------------------------------------------------------------------------------------
# part two
# -------------------------------------------------------------------------------------------------
def build_in_degree(rules, update):
    in_degree = {num: 0 for num in update}
    
    for i, j in rules:
        if i in update and j in update:
            in_degree[j] += 1
            
    return in_degree

def get_ordered_sequence(rules, update):
    in_degree = build_in_degree(rules, update)
    result = []
    
    while in_degree:
        for num in list(in_degree.keys()):
            if in_degree[num] == 0:
                result.append(num)
                in_degree.pop(num, None)
                for i, j in rules:
                    if i == num and j in in_degree:
                        in_degree[j] -= 1
                break
                
    return result

part_two_total = 0
for update in updates:
    if not verify_update(update):
        # in_degree = build_in_degree(rules, update)
        # print(in_degree)
        sequence = get_ordered_sequence(rules, update)
        part_two_total += sequence[len(sequence)//2]
print(part_two_total)

