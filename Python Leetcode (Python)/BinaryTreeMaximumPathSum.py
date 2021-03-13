# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxValue = root.val
        self.maxHelper(root)
        return self.maxValue
        
    def maxHelper(self, root):
        if not root:
            return 0
        left = self.maxHelper(root.left)
        right = self.maxHelper(root.right)
        tempMax = max(root.val, root.val+left, root.val+right)
        self.maxValue = max(self.maxValue,tempMax, root.val+left+right)
        return tempMax