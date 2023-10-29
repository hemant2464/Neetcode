class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        possible_sums = {0}
        for num in nums:
            new_sums = set()
            for pos_sum in possible_sums:
                new_sums.add(pos_sum + num)
                if pos_sum + num == target:
                    return True
            possible_sums.update(new_sums)
        return False