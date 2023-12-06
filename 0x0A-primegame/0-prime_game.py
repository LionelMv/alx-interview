#!/usr/bin/python3
"""
Prime Game
"""

def is_prime(num):
    """Checks if a number is a prime number.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    x: the number of rounds.
    nums: an array of n.
    Return:
        name of the player that won the most rounds.
        If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))

        # Determine the winner based on the count of prime numbers
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
