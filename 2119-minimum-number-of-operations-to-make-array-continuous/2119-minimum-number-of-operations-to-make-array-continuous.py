import bisect
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        running_maximum = 0
        for i, num in enumerate(nums):
            if len(nums) - i < running_maximum:
                break
            running_maximum = max(bisect.bisect_left(nums, num + n) - i, running_maximum)
        return n - running_maximum