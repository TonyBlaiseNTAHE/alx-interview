#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    else:
        t = [[1]]
        for i in range(1, n):
            row = [1]
            for k in range(1, i):
                row.append(t[i-1][k-1] + t[i-1][k])
            row.append(1)
            t.append(row)
        return t

