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
    unlocked = []
    keys = set()
    i = 0
    box_length = len(boxes)

    while i < box_length:
        oldi = i
        unlocked.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < box_length and key not in unlocked:
                i = key
                break
            
        if oldi != i:
            continue
        else:
            break

    for i in range(box_length):
        if i not in unlocked:
            return False
    return True
