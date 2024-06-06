#!/usr/bin/python3

""" You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes. """


def canUnlockAll(boxes):
    """ Return True if all boxes can be opened, else return False """
    if boxes is None:
        return False

    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()

        if current_box not in visited:
            visited.add(current_box)

            for key in boxes[current_box]:
                if 0 <= key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n
