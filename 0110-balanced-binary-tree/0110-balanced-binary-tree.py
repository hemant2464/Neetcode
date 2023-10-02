class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0
            
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)
            
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
            current_height = 1 + max(left_height, right_height)
            
            return balanced, current_height
        
        return dfs(root)[0]