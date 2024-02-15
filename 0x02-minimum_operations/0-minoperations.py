#!/usr/bin/python3
"""import libraries"""


def minOperations(n):
    """calculates the fewest number of operations needed to result"""
    if (n <= 1):
        return 0

    count = 2
    while True:
        if (n == count):
            return count
