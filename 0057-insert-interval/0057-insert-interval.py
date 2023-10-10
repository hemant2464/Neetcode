class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        inserted = False
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                merged.append(interval)
            elif interval[0] > newInterval[1]:
                if not inserted:
                    merged.append(newInterval)
                    inserted = True
                merged.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        if not inserted:
            merged.append(newInterval)
        
        return merged