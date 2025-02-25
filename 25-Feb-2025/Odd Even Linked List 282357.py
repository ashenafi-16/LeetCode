# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode(-1)
        cur = new_node
        st = cur
        pos = head
        iterator = 0
        while pos:
            if iterator % 2 == 0:
                cur.next = ListNode(pos.val)
                cur = cur.next
            iterator += 1
            pos = pos.next
        iterator = 0
        pos = head
        while pos:
            if iterator % 2 != 0:
                cur.next = ListNode(pos.val)
                cur = cur.next
            iterator += 1
            pos = pos.next
        return st.next