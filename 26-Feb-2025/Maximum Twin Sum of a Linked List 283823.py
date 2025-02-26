# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        slow  = head
        fast = head
        cur = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = pre  
            pre = temp
        
        maximum = float('-inf')
        while cur and pre:
            if (cur.val + pre.val) > maximum:
                maximum = (cur.val + pre.val)
            cur = cur.next
            pre = pre.next
        # while cur:
        #     print(cur.val)
        #     cur = cur.next
        # print(pre.val)
        return maximum

