class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach_indices = [nums[i] + i for i in range(len(nums))]
        left, right, jumps = 0, 0, 0

        while right < len(nums) - 1:
            jumps += 1
            left, right = right + 1, max(max_reach_indices[left:right + 1])

        return jumps