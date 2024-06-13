#!/usr/bin/env python3
"""Minimum Operations
"""


def minOperations(n):
    """
    args:
      n: the number of time
    """
    op = 0
    div = 2

    while n > 1:
        while n % div == 0:
            op += div
            n //= div
        div += 1
    return op
