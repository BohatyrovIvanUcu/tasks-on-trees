# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root):
        def find_common_node(node):
            if node is None:
                return None, 0
            
            left_node, left_depth = find_common_node(node.left)
            right_node, right_depth = find_common_node(node.right)
            
            if left_depth == right_depth:
                return node, left_depth + 1
            elif left_depth > right_depth:
                return left_node, left_depth + 1
            else:
                return right_node, right_depth + 1
        
        result, _ = find_common_node(root)
        return result
