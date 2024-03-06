#!/usr/bin/python3
"""
A function that returns a list of integers representing
the Pascal's triangle of n.
Returns an empty list if n <= 0

Solution:
The first row is [1]
The second row is [1][1]
The third row is [1][2][2][1]
Addition done to the numbers just above the cell
We can add [0] at both ends of the previous row so that it flows with the code.
e.g. temp = [0] + previous_row + [0]
"""


def pascal_triangle(n):
    """returns Pascal's triangle in a list of list"""
    if n <= 0:
        return []

    # The first row
    my_list = [[1]]

    for i in range(n - 1):
        temp = [0] + my_list[-1] + [0]
        row = [temp[j] + temp[j+1] for j in range(len(my_list[-1]) + 1)]
        my_list.append(row)
    return my_list
