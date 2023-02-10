#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    totalH = 1
    copiedH = 0
    sum_ops = 0

    while totalH < n:
        if copiedH == 0:
            copiedH = totalH
            totalH = copiedH + totalH
            sum_ops += 2
            continue

        Hleft = n - totalH
        if Hleft < copiedH:
            return 0

        if Hleft % totalH != 0:
            totalH = copiedH + totalH
            sum_ops += 1
        else:
            copiedH = totalH
            totalH = copiedH + totalH
            sum_ops += 2

    if totalH == n:
        return sum_ops
    else:
        return 0
