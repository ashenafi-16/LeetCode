# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(fir,sec):
            
            if not fir and not sec:
                return True
            if not fir or not sec:
                return False
            
            
            return ((fir.val == sec.val) and 
            rec(fir.left,sec.right) and 
            rec(fir.right,sec.left))
            
        if not root:
            return True
        return rec(root.left,root.right)
       