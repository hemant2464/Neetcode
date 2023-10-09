import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums[:k]
        heapq.heapify(self.stream)
        for num in nums[k:]:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heapq.heappush(self.stream, val)
        elif val > self.stream[0]:
            heapq.heappushpop(self.stream, val)
        return self.stream[0]