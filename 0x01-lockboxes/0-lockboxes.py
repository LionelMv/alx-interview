#!/usr/bin/python3

"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.

This method determines if all the boxes can be opened.
 - boxes is a list of lists
 - A key with the same number as a box opens that box
    * You can assume all keys will be positive integers
 - There can be keys that do not have boxes
 - The first box boxes[0] is unlocked
 - Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
