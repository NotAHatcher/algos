# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = head
        r = head
        prev = None
        for i in range(n-1):
            r = r.next
        while r.next:
            prev = l
            l = l.next
            r = r.next
        if prev:
            prev.next = l.next
        else:
            head = l.next
        del(l)
        return head