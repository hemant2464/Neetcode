class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head==None): return head
        if (head.next==None): return head
        res = Solution.reverseList(self,head.next)
        head.next.next=head
        head.next=None
        return res