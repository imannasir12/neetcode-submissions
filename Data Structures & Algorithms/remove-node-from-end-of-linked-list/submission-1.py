class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        target_index = count - n # this is the index we want to stop at

        if target_index == 0:
            return head.next

        k = 1
        curr = head
        while k != target_index:
            curr = curr.next
            k += 1

        curr.next = curr.next.next

        return head