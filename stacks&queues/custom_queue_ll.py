class Node:
    def __init__(self, value):
        self.value = value
        self.next: "Node | None" = None
    
    def __str__(self):
        return f"(Node: value = {self.value})"


class Queue:
    def __init__(self):
        self.first: Node | None = None
        self.last: Node | None = None
        self.length = 0

    def __str__(self):
        return f"Queue: first = {self.first}, last = {self.last}, length = {self.length}"

    def peek(self) -> int | None:
        """Return the value at the front of the queue without removing it."""
        return self.first.value if self.first else None

    def enqueue(self, value) -> None:
        """Add a value to the end of the queue."""
        new_node = Node(value)

        if self.last:
            self.last.next = new_node
        else:
            self.first = new_node

        self.last = new_node
        self.length += 1

    def dequeue(self) -> int | None:
        """Remove and return the value at the front of the queue."""
        if not self.first:
            return None

        removed_value = self.first.value

        self.first = self.first.next
        if not self.first:
            self.last = None

        self.length -= 1

        return removed_value

    def is_empty(self):
        """Check if the queue is empty."""
        return self.length == 0
    
    def print_queue(self):
        """Return a list of all values in the queue."""
        array = []
        current_node = self.first

        while current_node:
            array.append(current_node.value)
            current_node = current_node.next
        print(array)
        return array


my_queue = Queue()
print(my_queue.is_empty())
my_queue.print_queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(4)
my_queue.print_queue()
print(my_queue.dequeue())
print(my_queue.dequeue())
my_queue.print_queue()
