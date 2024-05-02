#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of coins
needed to meet a given amount total.

Used Dynamic programming the bottom up approach
"""


def makeChange(coins, total):
    """this functions determines the fewest number of coins needed to meet
    a given amount total - using coins of different values"""
    dp = [total + 1] * (total +1)
    dp[0] = 0

    for a in range(1, total + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
                # a = 7
                # coin = 3
                # dp[7] = 1 + dp[4]
    return dp[total] if dp[total] != total + 1 else -1
