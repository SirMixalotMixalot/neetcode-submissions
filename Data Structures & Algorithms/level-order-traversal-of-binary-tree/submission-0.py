# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        def add_to_level(node, level):
            nonlocal answer
            if node is None:
                return
            if len(answer) <= level:
                answer.append([])

            answer[level].append(node.val)

            add_to_level(node.left, level+1)
            add_to_level(node.right, level+1)

        add_to_level(root, 0)

        return answer
        