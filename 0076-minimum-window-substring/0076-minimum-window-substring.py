from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        target_counts = Counter(t)
        required_chars = len(target_counts)
        left, right = 0, 0
        formed_chars = 0
        ans = float("inf"), 0, 0

        while right < len(s):
            char = s[right]
            target_counts[char] -= 1
            if target_counts[char] == 0:
                formed_chars += 1

            while formed_chars == required_chars:
                window_size = right - left + 1
                if window_size < ans[0]:
                    ans = window_size, left, right + 1

                char = s[left]
                target_counts[char] += 1
                if target_counts[char] > 0:
                    formed_chars -= 1
                left += 1

            right += 1

        return s[ans[1]:ans[2]] if ans[0] != float("inf") else ""