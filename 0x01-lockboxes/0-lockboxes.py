#!/usr/bin/python3
"""
defines lockbox function
"""
def canUnlockAll(boxes):
    """
    This function determines whether all boxes can be unlocked
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    unlocked = [0]
    for i in range(len(boxes) - 1):
        for j in unlocked:
            for k in boxes[j]:
                if k not in unlocked:
                    unlocked.append(k)

    for i in range(len(boxes)):
        if i not in unlocked:
            return False
    
    return True
