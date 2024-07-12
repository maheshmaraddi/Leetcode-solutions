# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        q=deque()
        q.append(root)
        if not root:return []
        while q:
            leval =[]
            for i in range(len(q)):
                a = q.popleft()
                leval.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            l.append(leval[-1])
        return l
        