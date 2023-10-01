class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = l1
        carry = 0
        last = ListNode()  # Initialize a dummy node to keep track of the last node in the result list

        while l1 and l2:
            temp_sum = l1.val + l2.val + carry
            carry = temp_sum // 10
            l1.val = temp_sum % 10
            last = l1  # Update the last node
            l1 = l1.next
            l2 = l2.next

        if l2:  # If l2 has more nodes than l1, append the remaining nodes of l2 to the result
            last.next = l2
            l1 = l2

        while l1 and carry:
            temp_sum = l1.val + carry
            carry = temp_sum // 10
            l1.val = temp_sum % 10
            last = l1  # Update the last node
            l1 = l1.next

        if carry:  # If there's a remaining carry, add it as a new node
            last.next = ListNode(carry)

        return result