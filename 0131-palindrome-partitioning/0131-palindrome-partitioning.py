class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(start, partition):
            if start == len(s):
                ans.append(partition[:])
                return
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    partition.append(s[start:end + 1])
                    backtrack(end + 1, partition)
                    partition.pop()

        ans = []
        backtrack(0, [])
        return ans