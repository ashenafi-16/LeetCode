# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast= cur= head
        pre = None
        total_count = 0
        while head:
            total_count += 1
            head = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        while cur and slow != cur:
            temp = cur
            cur = cur.next
            temp.next = pre
            pre = temp
        if total_count % 2 != 0:
            slow = slow.next
        while pre != None and slow != None:
            if pre.val != slow.val:
                return False
            else:
                pre = pre.next
                slow = slow.next
        
        return True