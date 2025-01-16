# Working solution, Easy Leetcode Qn

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is None):
            return True
        elif q is not None and p is None:
            return False
        elif p is not None and q is None:
            return False
        elif p.val == q.val:
            return True and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        elif p.val != q.val:
            return False and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        