#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    A function to determine the winner between Maria and Ben in a prime game.
    Args:
        x (int): A parameter representing some value.
        nums (list): A list of integers.
    Returns:
        str or None: The name of the winner (Maria or Ben),
        or None if it's a tie.
    """
    if not nums or x <= 0:
        return None

    def sieve(n):
        """ Sieve of Eratosthenes to find all primes up to n """
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return is_prime

    def count_prime_multiples(primes, n):
        """ Count the moves in the game """
        visited = [False] * (n + 1)
        moves = 0
        for number in range(2, n + 1):
            if primes[number] and not visited[number]:
                moves += 1
                for multiple in range(number, n + 1, number):
                    visited[multiple] = True
        return moves

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
        else:
            moves = count_prime_multiples(primes, n)
            if moves % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
