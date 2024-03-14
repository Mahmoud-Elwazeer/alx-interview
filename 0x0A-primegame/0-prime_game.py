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


def get_prime_numbers(n):
    """get all prime numbers less than n """
    lst = [1]

    for i in range(2, n + 1):
        if (check_prime(i)):
            lst.append(i)

    return lst


def isWinner(x, nums):
    """name of the player that won the most rounds
        Maria and Ben are playing a game.
        Assuming Maria always goes first and both players play optimally
    """
    player1_out = []
    player2_out = []

    for i in nums:
        lst = get_prime_numbers(i)
        lst.sort(reverse=True)

        player1 = i
        try:
            lst.remove(player1)
        except Exception:
            pass

        count = 1
        for j in lst:
            if (count % 2 == 0):
                player1 = j
            else:
                player2 = j
            count += 1

        if (player1 == 1):
            player1_out.append(1)
            player2_out.append(0)

        elif (player2 == 1):
            player1_out.append(0)
            player2_out.append(1)

    if (sum(player1_out) > sum(player2_out)):
        return 'Maria'
    elif (sum(player1_out) < sum(player2_out)):
        return 'Ben'

    return None
