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
    if n <= 1:
        return 0

    # Initialize the array to store the minimum operations
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float('inf')  # Set to a large value initially
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
