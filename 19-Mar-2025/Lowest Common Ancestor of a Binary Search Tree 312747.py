# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.cur = None
        self.x = max(p.val,q.val)
        self.y = min(p.val,q.val)
        def bst(root):
            if not root:
                return None
            if root:
                if root.val < self.x and root.val < self.y:
                    return bst(root.right)
                elif root.val > self.x and root.val > self.y:
                    return bst(root.left)
                else:
                    return root
        return bst(root)
                    