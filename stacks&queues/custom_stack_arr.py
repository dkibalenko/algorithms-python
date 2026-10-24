from typing import Any


class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        length = len(self.data)
        return (
            f"Stack: head = {self.data[-1] if length > 0 else None}, "
            f"tail = {self.data[0] if length > 0 else None}, length = {length}"
        )

    def peek(self) -> Any | None:
        """Retrieves the very top element"""
        return self.data[-1] if self.data else None

    def push(self, value):
        """Adds an element to the top of the stack"""

        self.data.append(value)
        return self

    def pop(self):
        """Removes an element from the top of the stack"""

        if len(self.data) == 0:
            return None
        
        # when removing the last item
        removing_node = self.data.pop()

        return removing_node

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.data) == 0

    def print_stack(self) -> None:
        print(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return reversed(self.data)  # top to bottom



my_stack = Stack()
my_stack.push("Google")
my_stack.push("Udemy")
my_stack.push("Discord")
print(my_stack.peek())
my_stack.print_stack()
print(my_stack)

my_stack.pop()
my_stack.pop()
my_stack.print_stack()
# print(my_stack)
# print("Pop the last one")
# print(my_stack.pop())
# my_stack.print_stack()
