import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for node in lists:
            while node:
                heapq.heappush(min_heap, node.val)
                node = node.next
        
        dummy = ListNode(-1)
        current = dummy
        while min_heap:
            temp = ListNode(heapq.heappop(min_heap))
            current.next = temp
            current = current.next
        
        return dummy.next