from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < abs(target) or (s + target) % 2 != 0:
            return 0
        
        subset_sum = (s + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[subset_sum]