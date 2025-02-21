# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        cur = head
        pre = None
        while cur:
            
            
            if cur.val in seen:
                print(cur.val)
                pre.next = cur.next
            else:
                seen.add(cur.val)
                pre = cur
            
            cur = cur.next
        return head
