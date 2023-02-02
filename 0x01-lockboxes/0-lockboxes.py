#!/usr/bin/python3
"""
defines lockbox function
"""
def canUnlockAll(boxes):
    """
    This function determines whether all boxes can be unlocked
    """
    unlocked = [0]
    for i in range(len(boxes) - 1):
        for j in unlocked:
            for k in boxes[j]:
                if k not in unlocked:
                    unlocked.append(k)

    if len(boxes) == len(unlocked):
        return True
    else:
        return False
