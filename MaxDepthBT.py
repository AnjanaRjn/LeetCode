from typing import Optional  #A binary tree's maximum depth is the number of 
                             #nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: #if root is empty return 0
            return 0
        left = self.maxDepth(root.left) # else move to left and give maximum depth to the left 
        right = self.maxDepth(root.right) # same with right

        return 1 + max(left, right)