# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.cur_sum = 0
        self.arr = []
        def bst(root):
            if not root:
                return 0
            
            right = bst(root.right)
            self.cur_sum += root.val
            root.val = self.cur_sum
            left = bst(root.left)
        bst(root)
        return root
        