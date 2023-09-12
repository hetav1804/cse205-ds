class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        slow=fast=dummy
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        return slow.next