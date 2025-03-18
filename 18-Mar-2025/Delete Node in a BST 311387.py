# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minimum(val):
            cur= val
            while cur and cur.left:
                cur = cur.left
            return cur
                

        def delete(root):
            if not root:
                return
            if root.val < key:
                
                root.right = delete(root.right)
            elif root.val > key:
                root.left = delete(root.left)
            else:
                # print(root.val)
                if root and root.val == key:
                    if root.left and root.right:
                        node = minimum(root.right)
                        print(node.val)
                        root.val,node.val= node.val,root.val
                        
                        root.right = delete(root.right)
                        
                    elif root.left:
                        return root.left
                    elif root.right:
                        return root.right
                    else:
                        return None

            return root

        return delete(root)