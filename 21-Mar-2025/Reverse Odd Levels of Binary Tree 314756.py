# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def travers(node1, node2,n):
            if not node1 and not node2:
                return
            if n % 2 == 0:
                node1.val,node2.val = node2.val,node1.val

            travers(node1.left,node2.right,n+1)
           
            
            travers(node1.right,node2.left,n+1)
        
    
        travers(root.left, root.right,0)
        return root


            
