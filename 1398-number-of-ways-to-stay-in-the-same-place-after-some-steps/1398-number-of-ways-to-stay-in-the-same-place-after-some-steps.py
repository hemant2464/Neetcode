from functools import lru_cache

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        maxPos = min(steps // 2, arrLen - 1)
        
        @lru_cache(None)
        def dp(pos, stepsLeft):
            if stepsLeft == 0:
                return 1 if pos == 0 else 0
            ways = dp(pos, stepsLeft - 1) % MOD
            if pos > 0:
                ways = (ways + dp(pos - 1, stepsLeft - 1)) % MOD
            if pos < maxPos:
                ways = (ways + dp(pos + 1, stepsLeft - 1)) % MOD
            return ways
        
        return dp(0, steps)