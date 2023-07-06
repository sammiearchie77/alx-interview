#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""
def canUnlockAll(boxes):
    keys = set()
    for sublist in boxes:
        keys.update(sublist)
    return len(keys) == len(boxes)
