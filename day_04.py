def generate_grid(filename):
    grid = []
    with open(filename) as f:
        for line in f.readlines():
            grid.append([i for i in line.split()[0]])
    return grid


def build_directional_strings(grid, start_row, start_col):
    rows, cols = len(grid), len(grid[0])
    directions = {
        'up': (-1, 0),
        'up_right': (-1, 1),
        'right': (0, 1),
        'down_right': (1, 1),
        'down': (1, 0),
        'down_left': (1, -1),
        'left': (0, -1),
        'up_left': (-1, -1)
    }
    
    result = {}
    for direction, (dx, dy) in directions.items():
        current = ''
        row, col = start_row, start_col
        
        while 0 <= row < rows and 0 <= col < cols:
            current += grid[row][col]
            row += dx
            col += dy
            
        result[direction] = current
        
    return result



def part_one():
    grid = generate_grid('day_04.txt')

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':
                strings = build_directional_strings(grid, row, col)
                # print(strings)
                for key,value in strings.items():
                    if len(value)>=4 and value[:4]=='XMAS':
                        total+=1

    return total


# part_one()


def build_directional_strings(grid, start_row, start_col):
    # directions = [(-1, -1),(-1, 1),(1, 1),(1, -1)]
    direction_1 = [(-1,-1),(1,1),(1,1)] # top-left, center, bottom-right
    direction_2 = [(-1,1),(1,-1),(1,-1)] # top-right, center, bottom-left
    
    path_1 = ''
    current_row = start_row
    current_col = start_col
    for i in range(len(direction_1)):
        current_row += direction_1[i][0]
        current_col += direction_1[i][1]

        if current_row < 0 or current_row >= len(grid):
            continue
        if current_col < 0 or current_col >= len(grid[0]):
            continue
        
        path_1 += grid[current_row][current_col]

    path_2 = ''
    current_row = start_row
    current_col = start_col
    for i in range(len(direction_2)):
        current_row += direction_2[i][0]
        current_col += direction_2[i][1]

        if current_row < 0 or current_row >= len(grid):
            continue
        if current_col < 0 or current_col >= len(grid[0]):
            continue
        
        path_2 += grid[current_row][current_col]

        
    return (path_1, path_2)

from itertools import permutations

def part_two():
    grid = generate_grid('day_04.txt')
    perms = list(permutations(['M','S','M','S']))

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'A':
                path_1, path_2 = build_directional_strings(grid, row, col)
                if (path_1 == 'MAS' or path_1 == 'SAM') and (path_2 == 'MAS' or path_2 == 'SAM'):
                    # print(path_1, path_2, row, col)
                    total+=1

    return total

print(part_two()) # 1859 too high, 4928 too high
