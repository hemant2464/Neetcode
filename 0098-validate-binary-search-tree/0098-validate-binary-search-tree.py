class Solution:
    def isValidBST(self, root, minimum=float('-inf'), maximum=float('inf')):
        # Base case: root is null...
        if not root:
            return True

        # If the value of root is less than minimum or greater than maximum...
        if not minimum < root.val < maximum:
            return False

        # Recursively call the function for the left and right subtree...
        return (self.isValidBST(root.left, minimum, root.val) and
                self.isValidBST(root.right, root.val, maximum))