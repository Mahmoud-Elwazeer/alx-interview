#!/usr/bin/python3
"""import modules if found
"""


def makeChange(coins, total):
    """Change comes from within
    """
    if total == 0:
        return -1

    count = 0
    check = 0
    coins.sort(reverse=True)

    for coin in coins:
        while coin <= total and check <= total - coin:
            count += 1
            check += coin

    if check == total:
        return count
    else:
        return -1
