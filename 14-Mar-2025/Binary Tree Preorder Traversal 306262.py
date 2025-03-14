# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def preord(root,arr):
            if root:
                arr.append(root.val)
                preord(root.left,arr)
                preord(root.right,arr)
               
                    
        preord(root,arr)
        return arr
                    
