# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')

        def max_sum(root):
            if not root:
                return 0

            left_path_sum = max(max_sum(root.left), 0)
            right_path_sum = max(max_sum(root.right), 0)

            local_max = left_path_sum + right_path_sum + root.val
            self.max_path_sum = max(self.max_path_sum, local_max)

            return max(left_path_sum, right_path_sum) + root.val

        max_sum(root)
        return self.max_path_sum