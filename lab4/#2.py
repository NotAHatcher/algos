# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        ans = l
        r = 0
        while l1 or l2:
            if l1 and l2:
                r = (l1.val + l2.val + l.val) // 10
                l.val = (l1.val + l2.val + l.val) % 10
                if l1.next or l2.next or r:
                    temp = ListNode(r)
                    l.next = temp
                    l = temp
                l1 = l1.next
                l2 = l2.next
            elif l1:
                r = (l1.val + l.val) // 10
                l.val = (l1.val + l.val) % 10
                if l1.next or r:
                    temp = ListNode(r)
                    l.next = temp
                    l = temp
                l1 = l1.next
            else:
                r = (l2.val + l.val) // 10
                l.val = (l2.val + l.val) % 10
                if l2.next or r:
                    temp = ListNode(r)
                    l.next = temp
                    l = temp
                l2 = l2.next
        return ans