class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1
        
        low, high, half_len = 0, n1, (n1 + n2 + 1) // 2
        while low <= high:
            partition_nums1 = (low + high) // 2
            partition_nums2 = half_len - partition_nums1
            
            nums1_left = float('-inf') if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            nums1_right = float('inf') if partition_nums1 == n1 else nums1[partition_nums1]
            nums2_left = float('-inf') if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            nums2_right = float('inf') if partition_nums2 == n2 else nums2[partition_nums2]
            
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (n1 + n2) % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
                else:
                    return float(max(nums1_left, nums2_left))
            elif nums1_left > nums2_right:
                high = partition_nums1 - 1
            else:
                low = partition_nums1 + 1
        
        return 0  # If the input arrays are not sorted or empty, return 0