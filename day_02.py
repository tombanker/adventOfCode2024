filename = 'day_02.txt'
# filename = '2_test.txt'

def check_line(line):
    decreasing = True if line[0] > line[1] else False

    for i in range(len(line)-1):
        diff = abs(line[i]-line[i+1])

        if diff < 1 or diff > 3:
            return False

        if decreasing:
            if line[i] < line[i+1]:
                return False
        else:
            if line[i] > line[i+1]:
                return False

    return True

def part_one():
    total = 0
    with open(filename) as f:
        for line in f.readlines():
            line = [int(i) for i in line.split()]
            if check_line(line): total+=1
    return total


def part_two():
    total = 0
    with open(filename) as f:
        for line in f.readlines():
            line = [int(i) for i in line.split()]
            if check_line(line): 
                total+=1
            else:
                for i in range(len(line)):
                    tmp = line[:i] + line[i+1:]
                    if check_line(tmp):
                        total += 1
                        break
    return total


print(part_one())
print(part_two())
