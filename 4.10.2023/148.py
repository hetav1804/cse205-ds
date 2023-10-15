# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        x=ListNode(arr[0])
        e=1
        while e<len(arr):
            x.next=ListNode(arr[e])
            x=x.next
            e+=1
        return x