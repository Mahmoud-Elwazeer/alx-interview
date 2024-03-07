#!/usr/bin/python3
"""Island Perimeter"""

def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    lst = []

    for i in grid:
        lst.append(sum(i))

    len_x = max(lst)
    len_y = sum(lst) - max(lst) + 1

    return ((len_x + len_y) * 2)
