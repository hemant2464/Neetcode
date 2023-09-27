class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) # time: O(nlogn) space: O(n)
        res = 0
        last_time_taken = float("-inf") 
        for p, s in cars: # time O(n)
            time_taken = (target - p) / s
            if time_taken > last_time_taken:
                res += 1
                last_time_taken = time_taken

        return res
    # time: O(nlogn + n) = O(nlogn)
    # space: O(n)