class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_deficit = balance = start = 0
        n = len(gas)
        for i in range(n):
            balance += gas[i] - cost[i]
            if balance < 0:
                total_deficit += balance
                start = i + 1
                balance = 0
        if total_deficit + balance >= 0:
            return start
        return -1