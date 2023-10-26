class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first, second = cost[0], cost[1]
        for i in range(2, n):
            current = cost[i] + min(first, second)
            first, second = second, current
        return min(first, second)