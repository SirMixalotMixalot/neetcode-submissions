# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        maxDiff = 0
        def getHeight(node):
            nonlocal maxDiff
            if node is None:
                return 0
            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)

            print(leftHeight, rightHeight)

            maxDiff = max(maxDiff, abs(rightHeight - leftHeight))

            if maxDiff > 1:
                return False

            return 1 + max(leftHeight, rightHeight)
        getHeight(root)
        print(maxDiff)
        if maxDiff > 1:
            return False
        
        return True

        