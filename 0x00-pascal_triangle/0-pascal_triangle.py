#!/usr/bin/python3
"""
pascal_triangle
"""
def pascal_triangle(n):
    """pascal_triangle"""
    if n <= 0:
        return []

    result = []

    for i in range(1,n+1):
        item = []
        for j in range(i):
            if (j == 0 or j == i - 1):
                item.append(1)
            else:
                temp = result[i-2][j] + result[i-2][j-1]
                item.append(temp)
        result.append(item)

    return (result)

