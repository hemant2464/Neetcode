class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums):
            prev, curr = 0, 0
            for num in nums:
                prev, curr = curr, max(prev + num, curr)
            return curr

        if len(nums) == 1:
            return nums[0]

        max1 = rob_linear(nums[:-1])
        max2 = rob_linear(nums[1:])

        return max(max1, max2)