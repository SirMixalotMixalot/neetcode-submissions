# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# if i have a left, invert it and then if i have a right, invert it 
# and then swap the two pointers
# if i am null, return null
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        if not root.left and not root.right:
            return root # we are a leaf node 
        if root.left != None:
            root.left = self.invertTree(root.left)
        if root.right != None:
            root.right = self.invertTree(root.right)
        temp = root.left
        root.left = root.right 
        root.right = temp

        return root
        