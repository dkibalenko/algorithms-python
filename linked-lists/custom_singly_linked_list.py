class Node:
    def __init__(self, value):
        self.value = value
        self.next: "Node | None" = None

    def __str__(self) -> str:
        return (
            "({class_name} value: {value}, next: {next})"
            .format(
                class_name=__class__.__name__,
                value=self.value,
                next=self.next
            )
        )


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def __str__(self) -> str:
        return (
            "{class_name} Head: {head}, Tail: {tail}, length: {length}"
            .format(
                class_name=__class__.__name__,
                head=self.head,
                tail=self.tail,
                length=self.length
            )
        )

    def append_item(self, value) -> None:
        """
        Appends a new node with the given value to the end of the linked list.
        """
        new_node = Node(value=value)

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend_item(self, value) -> None:
        """
        Prepends a new node with the given value to the beginning of the linked list.
        """
        new_node = Node(value=value)

        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_item(self, index, value) -> None:
        if 0 > index or index > self.length:  # allow insertion at the last node
            raise IndexError("Index is out bounds")
        
        if index == 0:
            return self.prepend_item(value)
        if index == self.length:
            return self.append_item(value)

        leader_node = self._traverse_to_index(index - 1)
        
        new_node = Node(value)
        new_node.next = leader_node.next  # place new node at index
        leader_node.next = new_node
        self.length += 1

        return new_node

    def _traverse_to_index(self, index: int) -> Node:
        current_node = self.head

        for _ in range(index):  # iteration times to before insertion point node
            current_node = current_node.next  # move pointer to node before insert point
        
        return current_node
    
    def remove_item(self, index):
        if 0 > index or index >= self.length:
            raise IndexError("Index is out bounds")

        if index == 0:
            deleting_node = self.head
            
            if self.length == 1:  # if there is only one node
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            leader_node = self._traverse_to_index(index - 1)

            deleting_node = leader_node.next
            
            # if last node is deleted, remove tail
            if index == self.length - 1:
                self.tail = leader_node
                leader_node.next = None
            else:
                leader_node.next = deleting_node.next

        self.length -= 1

        return deleting_node

    def reverse_ll(self):
        # [11 -> 10 -> 5 -> 16 -> 99]
        # to [99 -> 16 -> 5 -> 10 -> 11]

        if not self.head.next:
            return self.head

        # prev = self.head
        # curr = prev.next

        # while curr:
        #     next = curr.next  # hold the rest of list

        #     # start reversing
        #     curr.next = prev
        #     # move both pointers
        #     prev = curr
        #     curr = next

        # self.head.next = None  # head is tail now, connect it to None
        # self.head = prev  # move head to prev, which is head now

        prev = None
        curr = self.head

        # prev -> None, curr -> 1 -> 2 -> 3 -> None

        while curr:
            # keep the rest of the list
            next_node = curr.next

            # the actual reversal
            curr.next = prev
            
            # move the pointers forward
            prev, curr = curr, next_node

        #     # (after first loop): None <- 1  2 -> 3 -> None.
        #     # Now prev is at 1, and curr is at 2. The link from 1 to 2 is gone.
        #     # The loop continues until curr becomes None (when you've processed the last node).
        #     # At this point, prev will be pointing to the new head of the reversed list.
        #     # (final state): None <- 1 <- 2 <- 3. The head of the list is now 3.
        
        self.head.next = None
        self.head = prev

        return self

    def print_list(self):
        array = []
        current_node = self.head

        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next
        return array


l_list = LinkedList(10)
l_list.append_item(5)
l_list.append_item(16)
l_list.prepend_item(11)
l_list.insert_item(2, 99)
print(l_list.print_list())
print(l_list)
l_list.reverse_ll()
print(l_list.print_list())
print(l_list)
# l_list.remove_item(3)
# print(l_list.print_list())