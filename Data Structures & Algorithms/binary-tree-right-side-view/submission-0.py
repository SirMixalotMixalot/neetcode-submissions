# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def add_to_right_view(node, level):
            nonlocal answer
            if node is None:
                return
            
            if len(answer) <= level:
                answer.append(None)
            
            if answer[level] is None:
                answer[level] = node.val
            
            add_to_right_view(node.right, level + 1)
            add_to_right_view(node.left, level + 1)

        add_to_right_view(root, 0)
        
        return answer
        