# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp:
            if not stack:
                stack.append(temp.val)
            else:
                if temp.val > stack[-1]:
                    while  stack and temp.val > stack[-1]:
                        stack.pop()
                stack.append(temp.val)
            temp = temp.next
        new = ListNode(stack[0])
        temp = new
        for i in range(1,len(stack)):
            a = ListNode(stack[i])
            temp.next = a
            temp = temp.next
        return new


