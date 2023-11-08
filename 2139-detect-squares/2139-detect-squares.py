from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        self.point_count = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.point_count[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for y2 in self.point_count[x]:
            if y2 != y:
                temp_count = 0
                for x2 in (x + y2 - y, x + y - y2):
                    if x2 in self.point_count and y in self.point_count[x2] and y2 in self.point_count[x2]:
                        temp_count += self.point_count[x2][y] * self.point_count[x2][y2]
                count += temp_count * self.point_count[x][y2]
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)