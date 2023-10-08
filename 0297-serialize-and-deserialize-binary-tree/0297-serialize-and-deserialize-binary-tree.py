class Codec:
    def serialize(self, root: 'TreeNode') -> str:
        """Encodes a tree to a single string."""
        if not root: return 'n'
        return str(root.val) + ' ' + self.serialize(root.left) + ' ' + self.serialize(root.right)

    def deserialize(self, data: str) -> 'TreeNode':
        """Decodes your encoded data to tree."""
        q = collections.deque(data.split())

        def preorder() -> 'TreeNode':
            s = q.popleft()
            if s == 'n':
                return None

            root = TreeNode(int(s))
            root.left = preorder()
            root.right = preorder()
            return root

        return preorder()