class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"(Node: value = {self.value}, next = {self.next})"


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return f"Stack: head = {self.head}, tail = {self.tail}, length = {self.length}"

    def peek(self):
        """Retrieves the very top element"""
        return self.head

    def push(self, value):
        """Adds an element to the top of the stack"""

        vtx = Node(value)
        vtx.next = self.head  # 1. connect new node to head
        self.head = vtx  # 2. move head on top
        if self.length == 0:
            self.tail = self.head  # tail is at head when adding first vtx

        self.length += 1
        return self

    def pop(self):
        """Removes an element from the top of the stack"""

        if not self.head:
            return None
        
        removing_vtx = self.head

        # when removing the last item
        if self.head == self.tail:
            self.head, self.tail = None, None
            self.length = 0
        else:
        # the very top item is garbage collected since we remove reference to it, or we can return it
            self.head = self.head.next
            self.length -= 1

        return removing_vtx

    def is_empty(self):
        """Check if the stack is empty"""
        return self.length == 0

    def print_stack(self):
        array = []
        current_node = self.head

        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next
        print(array)
        return array


my_stack = Stack()
my_stack.push("Google")
my_stack.push("Udemy")
my_stack.push("Discord")
my_stack.print_stack()
print(my_stack)

# print(my_stack.peek())
my_stack.pop()
my_stack.pop()
my_stack.print_stack()
print(my_stack)
print("Pop the last one")
print(my_stack.pop())
my_stack.print_stack()
