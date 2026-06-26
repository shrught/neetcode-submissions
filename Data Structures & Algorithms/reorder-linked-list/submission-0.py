# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        #slow is at the midpoint
       
        p2 = slow.next
        prev = slow.next = None


        #reverse the second half of the list
        while p2:
            tmp = p2.next
            p2.next = prev
            prev = p2
            p2 = tmp

        p1, p2 = head, prev

        while p2:
            tmp1, tmp2 = p1.next, p2.next
            p1.next = p2
            p2.next = tmp1
            p1, p2 = tmp1, tmp2

              
        