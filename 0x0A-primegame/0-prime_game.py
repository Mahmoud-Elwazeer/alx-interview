#!/usr/bin/python3
"""Prime Game"""


def check_prime(n):
    """check number is prime or not"""
    if (n == 1 or n % 2 == 0) and n != 2:
        return False

    for i in range(3, n, 2):
        if (n % i == 0 and i != n):
            return False

    return True


def rm_multiples(n, lst):
    """removing that number and its multiples from the list."""
    for i in lst:
        if (i % n == 0):
            lst.remove(i)

    return lst


def isWinner(x, nums):
    """name of the player that won the most rounds
        Maria and Ben are playing a game.
        Assuming Maria always goes first and both players play optimally
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    
    Maria = 0
    Ben = 0
    for i in nums:
        lst = list(range(i + 1))
        count = 1

        while lst != [1]:
            for i in lst:
                if(check_prime(i)):
                    get_n = i
                    break

            if (count % 2 != 0):
                rm_maria = rm_multiples(get_n, lst)
                lst = rm_maria.copy()
            else:
                rm_ben = rm_multiples(get_n, lst)
                lst = rm_ben.copy()
            count += 1

        if (rm_maria == [1]):
            Maria += 1
        elif (rm_ben == [1]):
            Ben += 1

    if (Maria > Ben):
        return 'Maria'
    elif (Maria < Ben):
        return 'Ben'
    
    return None

