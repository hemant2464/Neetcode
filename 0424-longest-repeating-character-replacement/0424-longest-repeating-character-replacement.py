import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = left = 0
        char_count = collections.Counter()
        
        for right in range(len(s)):
            char_count[s[right]] += 1
            max_freq = max(max_freq, char_count[s[right]])
            
            if right - left + 1 > max_freq + k:
                char_count[s[left]] -= 1
                left += 1
        
        return len(s) - left