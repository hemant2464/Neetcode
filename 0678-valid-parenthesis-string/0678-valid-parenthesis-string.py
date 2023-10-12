class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right = 0, 0

        # From left to right scan, treat '*' as '('
        for char in s:
            if char in ['(', '*']:
                left += 1
            else:
                left -= 1
            if left < 0:
                return False

        # Reset left count for right to left scan, treat '*' as ')'
        left = 0
        
        # From right to left scan, treat '*' as ')'
        for char in reversed(s):
            if char in [')', '*']:
                right += 1
            else:
                right -= 1
            if right < 0:
                return False

        # Both left and right counts should be non-negative
        return left >= 0 and right >= 0