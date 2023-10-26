class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        N = len(nums)
        if N == 1:
            return nums[0]
        
        rob_next_plus_two = 0
        rob_next_plus_one = nums[N - 1]
        
        for i in range(N - 2, -1, -1):
            current = max(rob_next_plus_one, rob_next_plus_two + nums[i])
            rob_next_plus_two, rob_next_plus_one = rob_next_plus_one, current
            
        return rob_next_plus_one