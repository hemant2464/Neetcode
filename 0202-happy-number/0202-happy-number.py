class Solution:
    def digitSquareSum(self, n: int) -> int:
        digit_sum = 0
        while n > 0:
            digit = n % 10
            digit_sum += digit ** 2
            n //= 10
        return digit_sum
    
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        
        while True:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(self.digitSquareSum(fast))
            
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False