# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([root]) if root else []
        ans = []
        if not root:
            return []
        ans.append([root.val])
        while dq:
            temp = []
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    temp.append(node.left.val)
                    dq.append(node.left)
                if node.right:
                    temp.append(node.right.val)
                    dq.append(node.right)
            if temp:
                ans.append(temp)
        return ans
