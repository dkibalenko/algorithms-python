class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # add pointer to previous node
    
    def __str__(self) -> str:
        return (
            f"({__class__.__name__} value: {self.value}, "
            f"next: {self.next.value if self.next else None}, "
            f"prev: {self.prev.value if self.prev else None})"
        )



class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self) -> str:
        return (
            f"{__class__.__name__} Head: {self.head}, Tail: {self.tail}, "
            f"length: {self.length}"
        )

    def append_item(self, value):
        new_node = Node(value)

        # connect nodes
        new_node.prev = self.tail
        self.tail.next = new_node

        # move tail to new node
        self.tail = new_node

        self.length += 1

        return new_node
    
    def prepend_item(self, value):
        new_node = Node(value)

        # connect nodes
        new_node.next = self.head
        self.head.prev = new_node

        # move head to new node
        self.haed = new_node

        self.length += 1

        return new_node
    
    def _traverse_to_index(self, index: int) -> Node:
        current_node = self.head

        for _ in range(index):  # iteration times to before insertion point node
            current_node = current_node.next  # move pointer to node before insert point
        
        return current_node

    def insert_item(self, index, value):
        if 0 > index or index > self.length:  # allow insertion at the last node
            raise IndexError("Index is out bounds")
        
        if index == 0:
            return self.prepend_item(value)
        if index == self.length:
            return self.append_item(value)

        # node before insertion point
        leader = self._traverse_to_index(index - 1)
        
        new_node = Node(value)
        
        # node AT insertion point
        insertion_point = leader.next
        # connect new node to one AT insetion point
        new_node.next = insertion_point
        # connect aft to new node
        insertion_point.prev = new_node
        # connect leader to new node
        leader.next = new_node
        # connect new node to leader
        new_node.prev = leader

        return new_node

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
        # there is only one node
        if not self.head.next:
            return self.head
        
        prev = self.head
        curr = prev.next

        while curr:
            # hold the rest of the list
            next_node = curr.next

            # start reversing
            curr.next = prev

            # move pointers forward
            prev = curr
            curr = next_node
        
        self.head.next = None
        self.head = prev


    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        return self.length


my_ll = DoublyLinkedList(22)
my_ll.insert_item(0, 11)
my_ll.insert_item(1, 33)
my_ll.insert_item(2, 44)
my_ll.insert_item(2, 99)
print(my_ll)
