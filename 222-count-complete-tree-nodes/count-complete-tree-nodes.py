# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l=[]
        def pre(root):
            if root==None:
                return
            l.append(root.val)
            pre(root.left)
            pre(root.right)
        pre(root)
        return len(l)