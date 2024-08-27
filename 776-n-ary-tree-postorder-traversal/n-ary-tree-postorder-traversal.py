"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l=[]

        def t(root):
            if not root:return []
            if root.children:
                for i in root.children:
                    t(i)
            
            l.append(root.val)
        t(root)
        return l