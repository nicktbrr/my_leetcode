from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        while list1:
            if not list2:
                break
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        if list2:
            curr.next = list2
        elif list1:
            curr.next = list1
        return res.next

r1 = ListNode(1)
r1.next = ListNode(2)
r1.next.next = ListNode(4)

r2 = ListNode(1)
r2.next = ListNode(2)
r2.next.next = ListNode(4)

r3 = ListNode(1)
r4 = ListNode(2)
# print(Solution().mergeTwoLists(r1, r2))
print(Solution().mergeTwoLists(r3,r4))
