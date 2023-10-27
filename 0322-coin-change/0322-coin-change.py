from math import inf, isinf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def nfewest(amt):
            if amt < 0:
                return inf
            elif amt == 0:
                return 0
            else:  # amt > 0
                return min(1 + nfewest(amt - c) for c in coins)

        n = nfewest(amount)
        return -1 if isinf(n) else n