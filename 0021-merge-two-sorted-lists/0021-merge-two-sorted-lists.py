class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        current_node = new_list
        while True:
            if list1 is None:
                current_node.next = list2
                break
            if list2 is None:
                current_node.next = list1
                break
            if list1.val > list2.val:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
            else:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            current_node = current_node.next
        return new_list.next