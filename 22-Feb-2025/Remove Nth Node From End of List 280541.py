# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pos = head
        count = 0
        while pos:
            count += 1
            pos = pos.next
        count = count - n
        cur = head
        pre = None
        while cur and count != 0:
            pre = cur
            cur= cur.next
            count -= 1
        if pre:
            if pre.next:
                pre.next = cur.next
        else:
            head = head.next
        return head
        
        