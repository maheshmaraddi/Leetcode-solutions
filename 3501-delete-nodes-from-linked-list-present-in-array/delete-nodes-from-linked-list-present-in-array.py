# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        l= set(nums)
        t = ListNode(-1)
        t.next = head
        cur=head
        prev=t
        while cur:
            if cur.val in l:
                prev.next = cur.next
                cur.next = None
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return t.next
        