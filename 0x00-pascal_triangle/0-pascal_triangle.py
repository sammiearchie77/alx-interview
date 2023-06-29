#!/usr/bin/python3
"""
    Pascal's Triangle
    Create a function def pascal_triangle(n): 
    that returns a list of lists of integers 
    representing the Pascal’s triangle of n:
        - Returns an empty list if n <= 0
        - You can assume n will be always an integer
"""

def pascal_triangle(n):
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle