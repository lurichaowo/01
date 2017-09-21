def de_grid(grid):
    string = ''
    i = 0
    while (i < len(grid[0])): #i = y value
        for x in grid:
            string = string + x[i] # add character to string
        string = string + '\n'# to skip lines
        i = i + 1
    return string 


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

    
print(de_grid(grid))