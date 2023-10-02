class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the root is None, return None
        if not root:
            return None
        
        # Recursive calls to invert the left and right subtrees
        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)
        
        # Swap the left and right subtrees
        root.left, root.right = inverted_right, inverted_left
        
        return root