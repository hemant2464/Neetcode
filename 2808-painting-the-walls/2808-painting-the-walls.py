from typing import List

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        postfix_times = [0] * n
        postfix_times[n - 1] = time[n - 1]

        for i in range(n - 2, -1, -1):
            postfix_times[i] = postfix_times[i + 1] + time[i]

        memo = [[-1] * (n + 1) for _ in range(n)]

        def dp(index, time_painted):
            if index == n:
                return 0 if time_painted >= 0 else float('inf')

            if time_painted >= n - index:
                return 0

            if time_painted + postfix_times[index] < 0:
                return float('inf')

            if memo[index][time_painted] != -1:
                return memo[index][time_painted]

            memo[index][time_painted] = min(
                dp(index + 1, time_painted - 1),
                cost[index] + dp(index + 1, time_painted + time[index])
            )

            return memo[index][time_painted]

        return dp(0, 0)