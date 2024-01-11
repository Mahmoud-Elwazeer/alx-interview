#!/usr/bin/python3
"""lockboxes"""

def canUnlockAll(boxes):
    for i in range(1, len(boxes)):
        flag = 0
        for j in boxes:
            if (i in j):
                flag = 1
                break
        if (flag == 0):
            return False
        
    return True
