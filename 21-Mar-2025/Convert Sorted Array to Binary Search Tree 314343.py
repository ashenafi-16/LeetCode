# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(nums):
            if not nums:
                return 
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = divide(nums[:mid])
            root.right = divide(nums[mid+1:])
            return root
        return divide(nums)


