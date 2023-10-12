#!/usr/bin/python3
"""Calculate the fewest number of operations needed
    to result in exactly n H characters in the file
    using Copy All and Paste operations."""


def minOperations(n):
    """
    Calculate the fewest number of operations needed
    to result in exactly n H characters in the file
    using Copy All and Paste operations.

    Args:
    n (int): The target number of H characters to achieve.

    Returns:
    int: The minimum number of operations required
        to reach n H characters. If n is impossible to achieve, return 0.
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
        b += 1
    return a
