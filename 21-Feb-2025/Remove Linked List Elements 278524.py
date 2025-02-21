# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        if head and head.val == val:
            head = head.next
            
        return head
