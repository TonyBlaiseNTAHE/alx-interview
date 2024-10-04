#!/usr/bin/python3
"""
A function that return a lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Pascal triangle"""
    prototype = [[1]]
    if n <= 0:
        return []
    else:
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(prototype[i-1][j-1] + prototype[i-1][j])
            row.append(1)
            prototype.append(row)
        return prototype
