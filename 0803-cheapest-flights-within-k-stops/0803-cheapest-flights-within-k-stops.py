from typing import List
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        costs = [float('inf') for _ in range(n)]
        costs[src] = 0

        for _ in range(k + 1):
            temp = costs.copy()
            for u in range(n):
                for v, w in graph[u]:
                    temp[v] = min(temp[v], costs[u] + w)
            costs = temp

        return temp[dst] if temp[dst] != float('inf') else -1