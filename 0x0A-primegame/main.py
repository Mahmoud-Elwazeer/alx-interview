#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

nums = [0] * 5
for i in range(5):
    nums[i] = i * i

print("Winner: {}".format(isWinner(100, nums)))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
