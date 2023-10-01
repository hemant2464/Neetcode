class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_ptr, fast_ptr = head, head
        
        while fast_ptr and fast_ptr.next: 
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            
            if fast_ptr == slow_ptr: 
                return True
        
        return False