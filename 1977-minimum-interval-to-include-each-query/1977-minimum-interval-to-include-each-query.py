import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
        queries = sorted(((q, i) for i, q in enumerate(queries)))  # Sort queries with their indices

        min_heap = []
        res = [-1] * len(queries)  # Initialize result list with -1

        i = 0
        for q, q_idx in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))  # Store interval length and end time in min_heap
                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                res[q_idx] = min_heap[0][0]  # Store the minimum interval length for the current query

        return res