# keep track of the nodes to the left and right of the current node
# we have a value associated with a node

#        9
#    4       20
#  1   6  15   170
from typing import Any


class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

    def __repr__(self):
        return str(f"Node({self.v})")


class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def insert(self, v):
        # the pointer to reference from
        current_node = None
        # initialize a new noe
        new_node = Node(v)

        # if tree is empty, set new node as the root
        if self.root is None:
            self.root = new_node
        else:
            # walk down the tree from the root
            current_node = self.root  # start with the root
            while True:
                if v < current_node.v:
                    # go left
                    if current_node.left is None:
                        current_node.left = new_node
                        return self
                    # keep walking down the tree - reset the current node
                    current_node = current_node.left
                else:
                    # go right
                    if current_node.right is None:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, v):
        # returns the node we are looking for or None
        if not self.root:
            return

        current_node = self.root
        # traverse the tree
        while current_node:
            if v < current_node.v:
                # go left
                current_node = current_node.left
            elif v > current_node.v:
                # go right
                current_node = current_node.right
            else:
                return current_node

    def remove(self, v):
        if not self.root:
            return False

        curr = self.root
        parent = None

        # 1. Find the node to remove
        while curr:
            if v < curr.v:
                parent = curr
                curr = curr.left
            elif v > curr.v:
                parent = curr
                curr = curr.right
            else:
                # ---- CASE 1: No right child ----
                if curr.right is None:
                    if parent is None:
                        self.root = curr.left
                    else:
                        if curr.v < parent.v:
                            parent.left = curr.left
                        else:
                            parent.right = curr.left

                # ---- CASE 2: Right child with no left child ----
                elif curr.right.left is None:
                    curr.right.left = curr.left
                    if parent is None:
                        self.root = curr.right
                    else:
                        if curr.v < parent.v:
                            parent.left = curr.right
                        else:
                            parent.right = curr.right

                # ---- CASE 3: Right child has a left subtree ----
                else:
                    # Find leftmost node in right subtree
                    leftmost = curr.right.left
                    leftmost_parent = curr.right

                    while leftmost.left:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    # Rewire leftmost's parent's left subtree
                    leftmost_parent.left = leftmost.right

                    # Move children
                    leftmost.left = curr.left
                    leftmost.right = curr.right

                    if parent is None:
                        self.root = leftmost
                    else:
                        if curr.v < parent.v:
                            parent.left = leftmost
                        else:
                            parent.right = leftmost
                return True
        return False

    def bfs(self) -> list:
        curr = self.root
        visited = []  # to store the values of the nodes in the order they were visited
        queue = []  # to keep track of the nodes to visit next (children of the current node)

        if curr:
            queue.append(curr)

        while queue:
            # O(n) shifts all remaining elements left
            curr = queue.pop(0)  # get first node
            visited.append(curr.v)  # add curr node's value
            print(curr)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return visited

    def bfsr(self, queue: list, visited: list = []) -> list:
        if not queue:
            return visited

        curr = queue.pop(0)  # O(n) shifts all remaining elements left
        visited.append(curr.v)
        print(curr)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

        return self.bfsr(queue, visited)


def traverse(node: Node) -> dict[str, Any]:
    """
    Recursively traverse a binary search tree and return a dictionary
    representing the structure of the tree.
    """
    if node is None:
        return None

    tree = {"value": node.v}
    # recursively traverse the left and right subtrees
    tree["left"] = traverse(node.left)
    tree["right"] = traverse(node.right)

    return tree

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# tree.bfs()
# tree.bfsr(queue=[tree.root], visited=[])
# print(tree.lookup(4))

print(traverse(tree.root))

#        9
#    4      20
#  1   6 15   170
