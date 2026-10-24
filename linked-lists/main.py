class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link nodes using pointers (references)
node1.next = node2  # node1 points to node2
node2.next = node3  # node2 points to node3

# Head pointer points to the first node
head = node1

# Traverse
current = head

while current:
    print(current.data)
    current = current.next
