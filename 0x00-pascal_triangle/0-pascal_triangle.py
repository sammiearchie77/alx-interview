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
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]
        
        for j in range(1, i):
            current_row.append(prev_row[j-1] + prev_row[j])
        
        current_row.append(1)
        triangle.append(current_row)
    
    return triangle