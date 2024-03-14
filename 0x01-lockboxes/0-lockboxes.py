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
    # Initialize a set to keep track of visited boxes
    visited = set()
    # Initialize a queue to perform BFS
    queue = [0]  # Start with the first box
    # Mark the first box as visited
    visited.add(0)

    # Continue BFS until the queue is empty
    while queue:
        # Pop the front of the queue
        current_box = queue.pop(0)
        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to an unvisited box
            if key not in visited and key < len(boxes):
                # Mark the box as visited
                visited.add(key)
                # Add the box to the queue for further exploration
                queue.append(key)

    # If all boxes have been visited, return True, otherwise return False
    return len(visited) == len(boxes)
