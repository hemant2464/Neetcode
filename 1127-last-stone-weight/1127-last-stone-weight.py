import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = [-stone for stone in stones]
        heapq.heapify(res)
        while len(res) > 1:
            a = heapq.heappop(res)
            b = heapq.heappop(res)
            heapq.heappush(res, -abs(a - b))
        return -res[0]