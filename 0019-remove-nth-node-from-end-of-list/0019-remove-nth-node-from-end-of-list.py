class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left_ptr = right_ptr = head
        
        # Move right pointer n nodes ahead
        for _ in range(n):
            right_ptr = right_ptr.next
        
        # If right pointer reached the end, remove the first node
        if not right_ptr:
            head = head.next
        else:
            # Move both pointers until right pointer reaches the end
            while right_ptr.next:
                left_ptr = left_ptr.next
                right_ptr = right_ptr.next
            
            # Remove the nth node from the end
            left_ptr.next = left_ptr.next.next
            
        return head