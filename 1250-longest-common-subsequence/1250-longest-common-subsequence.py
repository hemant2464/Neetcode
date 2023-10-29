class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            text1, text2, m, n = text2, text1, n, m
        dp = [[0] * (n + 1) for _ in range(2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
                else:
                    dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
        return dp[m % 2][n]