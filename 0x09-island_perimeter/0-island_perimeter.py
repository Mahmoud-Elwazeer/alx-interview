#!/usr/bin/python3
"""Island Perimeter"""

def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    size_y = len(grid)
    size_x = len(grid[0])
    perimeter = 0

    for i in range(size_y):
        for j in range(size_x):
            if grid[i][j] == 1:
                perimeter += 4
                if grid[i - 1][j] == 1:
                    perimeter -= 2
                if grid[i][j - 1] == 1:
                    perimeter -= 2

    return (perimeter)

