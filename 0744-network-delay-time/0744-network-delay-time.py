class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        inf = float('inf')
        dist = [inf] * (N + 1)
        dist[K] = 0

        for _ in range(N - 1):
            updated = False
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break

        max_time = max(dist[1:])
        return max_time if max_time < inf else -1