class My_Queue:
    def __init__(self):
        self._input = []  # input stack
        self._output = []  # output stack
    
    def __str__(self):
        return f"Queue: input = {self._input}, output = {self._output}"
    
    def enqueue(self, value):
        self._input.append(value)
    
    def dequeue(self):
        """
        Remove and return the value at the front of the queue. Amortized O(1).
        """
        self.peek()
        return self._output.pop()
    
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


my_queue = My_Queue()

my_queue.enqueue(1)  # first = [1]  last = []
my_queue.enqueue(2)  # first = [1, 2]  last = []
my_queue.enqueue(3)  # first = [1, 2, 3]  last = []
print(my_queue.peek())
print(my_queue)