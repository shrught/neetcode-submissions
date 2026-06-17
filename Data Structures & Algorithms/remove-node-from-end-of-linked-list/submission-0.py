# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(-1)
        dummy.next = head
        x = self.findFromEnd(dummy, n + 1)

        x.next = x.next.next
        return dummy.next

    



    def findFromEnd(self, head: ListNode, k:int) -> ListNode:
        p1 = head
        for i in range(k):
            p1 = p1.next
        p2 = head
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2

        