# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l=[]
        temp=head
        while  temp:
            l.append(temp.val)
            temp=temp.next
        left = l[:len(l)//2]
        right = l[len(l)//2:][::-1]
        # print(left,right)
        temp=head
        while temp:
            f=0
            while left and right:
                if f==0:
                    temp.val = left.pop(0)
                    temp=temp.next
                    f=1^f
                else:
                    temp.val = right.pop(0)
                    temp=temp.next
                    f=1^f
                
                # print(left,right)
            if left ==[] and right!=[]:
                temp.val = right.pop(0)
            else:
                if left!=[]:
                    temp.val =left.pop(0)
            temp=temp.next
        return head