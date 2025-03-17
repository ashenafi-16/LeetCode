# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.maxm = []
        
        if not root:
            return []
        self.dq = deque([root])
        self.maxm.append(root.val)
        while self.dq:
            l = len(self.dq)
            cur = float('-inf')
            for i in range(l):
                node = self.dq.popleft()
                if node.left:
                    self.dq.append(node.left)
                if node.right:
                    self.dq.append(node.right)
            for temp in self.dq:
                if cur < temp.val:
                    cur = temp.val
            self.maxm.append(cur)

                
        return self.maxm[:-1]