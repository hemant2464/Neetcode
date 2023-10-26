class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand_and_count_pallindromes(i, j, s):
            cnt = 0
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                cnt += 1
            return cnt
        
        return sum(expand_and_count_pallindromes(i, i, s) + expand_and_count_pallindromes(i, i + 1, s) for i in range(len(s)))