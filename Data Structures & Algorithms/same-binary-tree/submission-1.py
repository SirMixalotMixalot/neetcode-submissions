# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and p == q:
            return True
        if (p == None) ^ (q == None):
            return False
        
        if p and q and p.val != q.val:
            return False

        if p.left and q.left and p.left.val != q.left.val:
            return False
        if p.right and q.right and p.right.val != q.right.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        