# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        firstlist = list1
        secondlist = list2
        new_node = ListNode()
        head = new_node
        cur = head
        while firstlist and secondlist:
            if firstlist.val < secondlist.val:
                head.next = ListNode(firstlist.val)
                head = head.next
                firstlist = firstlist.next
            else:
                head.next = ListNode(secondlist.val)
                head = head.next
                secondlist = secondlist.next
        while firstlist:
            head.next = ListNode(firstlist.val)
            head = head.next
            firstlist = firstlist.next
        while secondlist:
            head.next = ListNode(secondlist.val)
            head = head.next
            secondlist = secondlist.next
           
                
        return cur.next

