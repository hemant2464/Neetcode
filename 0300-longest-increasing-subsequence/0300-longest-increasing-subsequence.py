from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            index = bisect_left(lis, num)
            if index == len(lis):
                lis.append(num)
            else:
                lis[index] = num
        return len(lis)