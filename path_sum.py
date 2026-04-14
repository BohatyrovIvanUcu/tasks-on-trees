# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum, currSum=0):
        if root is None:
            return False

        currSum += root.val

        if root.left is None and root.right is None:
            return currSum == targetSum

        left = self.hasPathSum(root.left, targetSum, currSum)
        right = self.hasPathSum(root.right, targetSum, currSum)

        return left or right
        
