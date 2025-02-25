# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        new_node = ListNode(-1)
        cur = new_node
        new = cur
        pos = head
        while pos:
            if pos.val < x:
                cur.next = ListNode(pos.val)
                cur = cur.next
            
            pos = pos.next
        pos = head
        while pos:
            if pos.val >= x:
                cur.next = ListNode(pos.val)
                cur = cur.next
            
            pos = pos.next
        return new.next