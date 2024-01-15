#!/usr/bin/python3
"""lockboxes"""


# def canUnlockAll(boxes):
#     """can unlock boxes"""
#     for i in range(1, len(boxes)):
#         flag = 0
#         for j in boxes:
#             if (i in j):
#                 flag = 1
#                 break
#         if (flag == 0):
#             return False

#     return True

def canUnlockAll(boxes):
    """can unlock boxes"""
    visited = set()

    # Helper function for DFS
    def dfs(box):
        """Mark the current box as visited"""
        visited.add(box)

        # Check the keys in the current box
        for key in boxes[box]:
            # If the key opens a box and the box hasn't been visited, recursively visit the box
            if key < len(boxes) and key not in visited:
                dfs(key)

    # Start DFS from the first box (box 0)
    dfs(0)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)

