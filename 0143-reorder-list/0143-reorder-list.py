class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        prev, curr = None, slow.next
        slow.next = None
        
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        head2 = prev

        head1 = head
        while head1 and head2:
            head1.next, head1 = head2, head1.next
            head2.next, head2 = head1, head2.next