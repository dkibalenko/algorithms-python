# 11 -> 10 -> 5 -> 16


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
        new_node = Node(value=value)
        
        new_node.prev = self.tail  # connect new node to previous (tail)
        self.tail.next = new_node  # connect tail to new node
        self.tail = new_node   # move tail to new node (the last one, now)

        self.length += 1
        return self

    def prepend_item(self, value):
        new_node = Node(value=value)

        new_node.next = self.head  # connect new node to head
        self.head.prev = new_node  # connect head to new node
        self.head = new_node  # move head at new node

        self.length += 1
        return self

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

        self.length += 1
        return self

    def remove_item(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")

        if index == 0:
            # node after head
            holding_node = self.head.next
            del self.head
            # move head to next node
            self.head = holding_node
        else:
            # reach to node before one being deleted
            leader = self.traverse_to_index(index - 1)
            # node being deleted
            deleting_node = leader.next

            # Update tail if removing last node
            if index == self.length - 1:
                self.tail = leader

            # node after one being deleted
            holding_node = deleting_node.next

            # connect leader with next node after one being deleted
            leader.next = holding_node

            del deleting_node

        self.length -= 1
        return self

    def print_list(self):
        array = []
        current_node = self.head

        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next
        return array


l_list = DoublyLinkedList(10)
l_list.append_item(5)
l_list.append_item(16)
l_list.prepend_item(11)
l_list.insert_item(0, 99)
# print(l_list.print_list())
# l_list.remove_item(3)
print(l_list)
print(l_list.print_list())
