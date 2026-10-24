class My_Queue:
    def __init__(self):
        self.main_stack = []  # main storage for the queue
        self.temp = []  # temporary buffer to help maintain FIFO order when enqueuing.
    
    def __str__(self):
        return f"Queue: first = {self.main_stack}, last = {self.temp}"
    
    def enqueue(self, value):
        """
        Add a value to the end of the queue. Time O(n).
        
        This method enqueues a value by moving all the elements from 
        the main stack to the temporary stack,
        adding the value to the main stack, and then moving all the elements 
        from the temporary stack back to the main stack.
        """
        while self.main_stack:
            self.temp.append(self.main_stack.pop())
        
        self.main_stack.append(value)

        while self.temp:
            self.main_stack.append(self.temp.pop())
    
    def dequeue(self):
        return self.main_stack.pop()
    
    def peek(self):
        return self.main_stack[-1]

    def empty(self):
        return not self.main_stack


class My_Queue:
    def __init__(self):
        self._input = []  # input stack, adds to the end of the queue
        self._output = []  # output stack, pops the front of the queue
    
    def __str__(self):
        return f"Queue: input = {self._input}, stack = {self._output}"
    
    def enqueue(self, value):
        self._input.append(value)  # add to the end of the queue
    
    def dequeue(self):
        self.peek()
        return self._output.pop()  # return the front of the queue
    
    def peek(self):
        """
        Return the front value

        If output stack is empty, transfer all items from input stack to output stack
        Then return the top element of the output stack

        Time O(1) amortized.
        """
        if not self._output:
            while self._input:
                self._output.append(self._input.pop())
        return self._output[-1]

    def empty(self):
        return not self._input and not self._output


class Queue:
    def __init__(self):
        # output stack (front of queue when non-empty) & input stack (new items)
        self.first: list = []  # output stack
        self.last: list = []  # input stack
    
    def __str__(self):
        return f"Queue: first = {self.first}, last = {self.last}"
    
    def _transfer_if_needed(self) -> None:
        """Transfer all items from input stack to output stack if output is empty."""
        if not self.first:
            while self.last:
                self.first.append(self.last.pop())

    def enqueue(self, value):
        """Add value to the end (rear) of the queue. Time O(1)"""

        self.last.append(value)

    def dequeue(self):
        """Remove and return the value at the front of the queue. Amortized O(1)."""
        self._transfer_if_needed()

        if not self.first:
            return None
        return self.first.pop()

    def peek(self):
        """Return the front value"""
        self._transfer_if_needed()
        return self.first[-1] if self.first else None

    def is_empty(self) -> bool:
        """Return True if queue is empty."""
        return not (self.first or self.last)


queue = Queue()
print(queue.is_empty())
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
# print(queue.peek())
print(queue)
