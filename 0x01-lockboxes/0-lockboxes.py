#!/usr/bin/python3

def canUnlockAll(boxes):
    """ A methods that determines if all the boxes can be opened"""
    n = len(boxes)
    stack = [0]
    unlocked = set()
    unlocked.add(0)

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
