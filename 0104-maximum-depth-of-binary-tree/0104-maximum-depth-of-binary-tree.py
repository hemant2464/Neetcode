# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = 0
        queue = deque([(root, 1)])
        
        while queue:
            current_node, current_depth = queue.popleft()
            max_depth = max(max_depth, current_depth)
            
            if current_node.left:
                queue.append((current_node.left, current_depth + 1))
            if current_node.right:
                queue.append((current_node.right, current_depth + 1))
        
        return max_depth