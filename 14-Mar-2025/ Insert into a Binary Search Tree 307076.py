# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root,val):
            if not root:
                root = TreeNode(val)
                return root
                
            if root:
                if val < root.val:
                    if root.left is None:
                        root.left = TreeNode(val)
                    else:

                        insert(root.left,val)
                else:
                    if root.right is None:
                        root.right = TreeNode(val)
                    else:
                        insert(root.right,val)
            return root
        return insert(root,val)
