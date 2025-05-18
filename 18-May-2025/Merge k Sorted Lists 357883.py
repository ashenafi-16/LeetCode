# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
       
        for i in range(len(lists)):
            if lists[i]:
                cur = lists[i]
                while cur:
                    heappush(arr,cur.val)
                    cur = cur.next
        head = ListNode(-1)
        cur = head
        while arr:
            node = heappop(arr)
            cur.next = ListNode(node)
            cur = cur.next
        return head.next


        