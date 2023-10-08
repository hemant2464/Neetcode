class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_index = {}
        preorder_index = 0
        
        for i, num in enumerate(inorder):
            root_index[num] = i
        
        def construct(left, right):
            nonlocal preorder_index
            
            if left > right:
                return None
            
            root_val = preorder[preorder_index]
            inorder_index = root_index[root_val]
            preorder_index += 1
            
            root = TreeNode(root_val)
            root.left = construct(left, inorder_index - 1)
            root.right = construct(inorder_index + 1, right)
            
            return root
        
        n = len(preorder) - 1
        return construct(0, n)