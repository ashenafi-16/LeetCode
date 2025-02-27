# Problem: Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        count = 0
        arr = []
        # if head:
        #     head = head.next
        # else:
        #     return False
        while head:
            
            if head in arr:
                return True
            arr.append(head)
            head = head.next
        # if cur:
        #     print(cur.val,count)
        # if not cur or count <= 1:
        #     return False
        return False