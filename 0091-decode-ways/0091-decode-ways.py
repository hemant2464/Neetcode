class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        length = len(s) - 1
        
        def get_result(index):
            if index > length:
                return 1
            if s[index] == '0':
                return 0
            if index in dp:
                return dp[index]
            single_letter = get_result(index + 1)
            word = 0
            if index < length and int(s[index] + s[index + 1]) <= 26:
                word = get_result(index + 2)
            dp[index] = single_letter + word
            return dp[index]
        
        return get_result(0)