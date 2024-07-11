# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ino(self,root):
        if root:
            return self.ino(root.left) + [root.val]+self.ino(root.right) 
        else:return []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=self.ino(root)
        for i in range(len(l)-1):
            if l[i]>=l[i+1]:return False
        return True
    
        
        