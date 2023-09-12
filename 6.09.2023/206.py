class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead = None
        while head != None:
            nxt = head.next
            head.next = reversedHead
            reversedHead = head
            head = nxt

        return reversedHead