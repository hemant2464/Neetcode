from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}  # O(n)
        for i, j in edges:
            graph.setdefault(i, []).append(j)
            graph.setdefault(j, []).append(i)

        queue = deque()  # O(n)
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                queue.append(node)

        while queue:  # O(n)
            current_node = queue.popleft()
            for neighbor in graph[current_node]:
                graph[neighbor].remove(current_node)
                if len(graph[neighbor]) == 1:
                    queue.append(neighbor)
            del graph[current_node]

        remaining_nodes = set(graph.keys())  # O(n)
        for i, j in reversed(edges):  # O(n)
            if i in remaining_nodes and j in remaining_nodes:
                return [i, j]