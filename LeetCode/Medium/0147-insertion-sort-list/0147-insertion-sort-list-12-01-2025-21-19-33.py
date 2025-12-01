# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp=head
        dummy=ListNode(-float('inf'))
        while tmp:
            next_node=tmp.next
            prev=dummy
            while prev.next and prev.next.val < tmp.val:
                prev=prev.next

            tmp.next=prev.next
            prev.next= tmp

            tmp=next_node
        return dummy.next