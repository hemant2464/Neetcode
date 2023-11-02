from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        memo = [[0] * n for _ in range(n)]
        
        def burst(left, right):
            if memo[left][right] > 0:
                return memo[left][right]
            
            if left + 1 == right:
                return 0
            
            maxCoins = 0
            for i in range(left + 1, right):
                coins = nums[left] * nums[i] * nums[right] + burst(left, i) + burst(i, right)
                maxCoins = max(maxCoins, coins)
            
            memo[left][right] = maxCoins
            return maxCoins
        
        return burst(0, n - 1)