# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.stk = []
        self.value = []
    
        def dfs(root):
            if not root: return 0
            self.stk.append(root)
            if self.stk[-1].left or self.stk[-1].right:
                pass
            else:
                temp = []
                for i in range(len(self.stk)):
                    temp.append(str(self.stk[i].val))
                self.value.append(''.join(temp))
                
            if root.left:
               dfs(root.left)
    
            if root.right:
                dfs(root.right)
            
            if self.stk:
                self.stk.pop()        
        dfs(root)
        res = 0
        for i in range(len(self.value)):
            res += int(self.value[i])
        return res

    

