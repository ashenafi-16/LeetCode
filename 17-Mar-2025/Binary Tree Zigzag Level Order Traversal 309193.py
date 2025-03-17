# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 1
        if not root:
            return []
        dq = deque([root])
        res = [[root.val]]
        while dq:
            length = len(dq)
               
            temp = []
            for i in range(length):
                node = dq.popleft()

                if node.left:
                    dq.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    dq.append(node.right)
                    temp.append(node.right.val)
            if temp:
                if level % 2 != 0:
                    res.append(temp[::-1])
                else:
                    res.append(temp)
            level += 1
        return res
            

