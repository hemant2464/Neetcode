class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create copy nodes and insert them in the original list
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Update random pointers for the copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the original and copied lists
        current = head
        new_head = head.next
        new_current = new_head
        
        while current:
            current.next = current.next.next
            current = current.next
            if new_current.next:
                new_current.next = new_current.next.next
                new_current = new_current.next
        
        return new_head