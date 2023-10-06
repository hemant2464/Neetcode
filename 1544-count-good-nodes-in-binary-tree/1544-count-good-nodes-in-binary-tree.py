class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float('-inf'))]
        count = 0

        while stack:
            node, max_num = stack.pop()

            if node.val >= max_num:
                count += 1

            max_num = max(max_num, node.val)

            if node.left:
                stack.append((node.left, max_num))
            if node.right:
                stack.append((node.right, max_num))

        return count