from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        mapping = {}
        queue = deque([node])

        # Create nodes and map original nodes to cloned nodes
        while queue:
            curr = queue.popleft()
            mapping[curr] = Node(curr.val, [])

            for neighbor in curr.neighbors:
                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)

        # Connect cloned nodes with cloned neighbors
        for original_node, cloned_node in mapping.items():
            for neighbor in original_node.neighbors:
                cloned_node.neighbors.append(mapping[neighbor])

        return mapping[node]