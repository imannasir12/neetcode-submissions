# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head # 0

        while curr:
            next = curr.next # 1
            curr.next = prev # None
            prev = curr # 0
            curr = next # 1

        return prev
        