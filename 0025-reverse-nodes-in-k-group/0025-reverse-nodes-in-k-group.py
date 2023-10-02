class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Count the total number of nodes in the linked list
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        
        # Calculate the number of groups to be reversed
        num_groups = count // k
        
        # Initialize pointers and dummy node
        prev = dummy = ListNode()
        dummy.next = head
        
        # Reverse each group of k nodes
        while num_groups:
            curr = prev.next
            nex = curr.next
            for _ in range(1, k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            num_groups -= 1
        
        return dummy.next