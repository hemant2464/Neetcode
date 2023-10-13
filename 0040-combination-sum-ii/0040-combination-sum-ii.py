from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Prune branches if candidate is greater than remaining target
                if candidates[i] > target:
                    break
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])

        candidates.sort()
        result = []
        backtrack(0, [], target)
        return result