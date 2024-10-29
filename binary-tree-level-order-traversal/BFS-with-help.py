# Implement BFS with some help

from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS 
        if not root: # empty
            return []
        
        result = []
        queue = deque([root])

        while queue:
            
            n = len(queue)
            level = []

            for i in range(n):
                parent = queue.popleft()
                level.append(parent.val)

                if parent.left:
                    queue.append(parent.left)
                if parent.right:
                    queue.append(parent.right)
            
            result.append(level)
        return result
