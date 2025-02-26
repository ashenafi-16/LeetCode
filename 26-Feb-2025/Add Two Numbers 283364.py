# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = []
        second = []
        cur = l1
        while cur:
            first.append(str(cur.val))
            cur = cur.next
        cur = l2
        while cur:
            second.append(str(cur.val))
            cur = cur.next
        value = str(int(''.join(first[::-1])) + int(''.join(second[::-1])))
        new_node = ListNode(-1)
        cur = new_node
        for i in range(len(value)-1,-1,-1):
            cur.next = ListNode(int(value[i]))
            cur = cur.next
        return new_node.next