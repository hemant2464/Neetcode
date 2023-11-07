class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        is_neg = x < 0
        x = abs(x)
        reversed_num = 0
        
        while x != 0:
            digit = x % 10
            if reversed_num > (INT_MAX - digit) // 10:
                return 0
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return -reversed_num if is_neg else reversed_num