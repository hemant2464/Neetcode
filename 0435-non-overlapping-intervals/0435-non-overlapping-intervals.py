class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # Sort intervals based on end points
        non_overlapping_count = 0
        end = float("-inf")  # Initialize the end variable with negative infinity

        for interval in intervals:
            if interval[0] >= end:
                # If the current interval doesn't overlap with the previous one
                non_overlapping_count += 1
                end = interval[1]  # Update the end variable

        # The number of overlapping intervals is the total intervals minus non-overlapping ones
        overlapping_count = len(intervals) - non_overlapping_count
        return overlapping_count