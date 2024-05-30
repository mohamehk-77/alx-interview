#!/usr/bin/python3
"""pascal_triangle"""


def pascal_triangle(n):
    """
        :type n: int
        :rtype: List[List[int]]
    """
    if n <= 0:
        return []
    res = [[1]]
    for i in range(n - 1):
        li = [1]
        for j in range(i):
            li.append(res[i][j]+res[i][j+1])
        li.append(1)
        res.append(li)
    return res
