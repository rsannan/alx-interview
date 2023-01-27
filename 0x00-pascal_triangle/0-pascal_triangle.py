#!/usr/bin/python3
"""
Defines a Pascal's Triangle function.

"""

def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    full_tri = [[1]]
    while len(full_tri) != n:
        tri = full_tri[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        full_tri.append(tmp)
    return full_tri
