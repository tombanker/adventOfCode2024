left = []
right = []

filename = 'day_01_test.txt'
filename = 'day_01.txt'

with open(filename) as f:
    for line in f.readlines():
        l,r = line.split()
        left.append(int(l))
        right.append(int(r))

def part_one(left, right):
    left = sorted(left)
    right = sorted(right)

    total = 0
    for l,r in zip(left, right):
        total += abs(l-r)

    return total

def part_two(left, right):
    total = 0
    for i in left:
        total += right.count(i) * i
    return total


print(part_one(left, right))
print(part_two(left, right))

import heapq

left_heap = left[:]
right_heap = right[:]
heapq.heapify(left_heap)
heapq.heapify(right_heap)

total = 0
while left_heap and right_heap:
    l = heapq.heappop(left_heap)
    r = heapq.heappop(right_heap)
    total += abs(l-r)
print(total)
