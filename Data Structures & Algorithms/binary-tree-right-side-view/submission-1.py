# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        answer = []
        while q:
            numberOfNodesInLevel = len(q)
            rightMostNode = None
            for _ in range(numberOfNodesInLevel):
                node = q.popleft()
                if node:
                    rightMostNode = node
                    q.append(node.left)
                    q.append(node.right)
            if rightMostNode:
                answer.append(rightMostNode.val)
        # def add_to_right_view(node, level):
        #     nonlocal answer
        #     if node is None:
        #         return
            
        #     if len(answer) <= level:
        #         answer.append(None)
            
        #     if answer[level] is None:
        #         answer[level] = node.val
            
        #     add_to_right_view(node.right, level + 1)
        #     add_to_right_view(node.left, level + 1)

        # add_to_right_view(root, 0)
        
        return answer
        