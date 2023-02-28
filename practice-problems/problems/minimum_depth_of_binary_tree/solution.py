# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):

        # Base case: not a node
        if root is None:
            return 0
        
        # Base case: if no children
        if root.left is None and root.right is None:
            return 1

        
        ld = float('inf')
        rd = float('inf')

        if root.left:
            ld = self.minDepth(root.left)
        
        if root.right:
            rd = self.minDepth(root.right)

        return 1 + min(ld, rd)
