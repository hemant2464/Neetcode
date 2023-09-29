class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_counts = {}
        current_counts = {}
        for char in set(s1):
            target_counts[char] = 0
            current_counts[char] = 0

        for char in s1:
            target_counts[char] += 1

        left = 0
        right = 0
        while right < len(s2):
            if s2[right] in target_counts:
                current_counts[s2[right]] += 1
                while current_counts[s2[right]] > target_counts[s2[right]]:
                    current_counts[s2[left]] -= 1
                    left += 1
                if right - left + 1 == len(s1):
                    return True
            else:
                current_counts = {char: 0 for char in set(s1)}
                left = right + 1

            right += 1

        return False