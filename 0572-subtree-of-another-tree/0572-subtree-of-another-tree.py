class Solution:
    def isSubtree_helper(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.isSubtree_helper(root1.left, root2.left) and self.isSubtree_helper(root1.right, root2.right)
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSubtree_helper(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)