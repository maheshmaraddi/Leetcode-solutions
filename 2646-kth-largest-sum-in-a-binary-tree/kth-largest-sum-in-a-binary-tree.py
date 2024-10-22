# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        q=[]
        q.append(root)
        while q:
            lev=[]
            for i in range(len(q)):
                a=q.pop(0)
                lev.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            res.append(lev)
        # print(res)
        res = sorted([sum(i) for i in res])
        if len(res)<k:
            return -1
        else:
            return res[-k]

        
        