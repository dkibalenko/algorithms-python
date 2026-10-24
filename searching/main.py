import timeit

# keep track of the nodes to the left and right of the current node
# we have a value associated with a node

#        9
#    4       20
#  1   6  15   170
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value      # information that is being stored in the tree
        self.left = left        # the left child (subtree)
        self.right = right      # the right child (subtree)

    def __repr__(self):
        return repr(f"Node({self.value})")


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

        curr = self.root
        # traverse the tree
        while curr:
            if v < curr.value:
                # go left
                curr = curr.left
            elif v > curr.value:
                # go right
                curr = curr.right
            else:
                return curr

    def remove(self, v):
        if not self.root:
            return False

        curr = self.root
        parent = None

        # 1. Find the node to remove
        while curr:
            if v < curr.value:
                parent = curr
                curr = curr.left
            elif v > curr.value:
                parent = curr
                curr = curr.right
            else:
                # ---- CASE 1: No right child ----
                if curr.right is None:
                    if parent is None:
                        self.root = curr.left
                    else:
                        if curr.value < parent.value:
                            parent.left = curr.left
                        else:
                            parent.right = curr.left

                # ---- CASE 2: Right child with no left child ----
                elif curr.right.left is None:
                    curr.right.left = curr.left
                    if parent is None:
                        self.root = curr.right
                    else:
                        if curr.value < parent.value:
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
                        if curr.value < parent.value:
                            parent.left = leftmost
                        else:
                            parent.right = leftmost

                return True

        return False


def traverse(node: Node):
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
# tree.insert(4)
# tree.insert(6)
# tree.insert(20)
# tree.insert(170)
# tree.insert(15)
# tree.insert(1)

# print(tree.lookup(4))

# print(traverse(tree.root))


def binary_search(nums: list[int], target: int) -> int:
    # set range to search
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (high + low) // 2
        guess = nums[mid]

        if guess == target:
            return mid  # return index of target
        
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# print(binary_search(numbers, 67))



def binary_search_recur(arr: list[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -1  # Base case: target not found

    mid = (left + right) // 2
    guess = arr[mid]

    if guess == target:
        return mid  # Base case: target found
    elif guess < target:
        return binary_search_recur(arr, target, mid + 1, right)  # discard left half
    else:
        return binary_search_recur(arr, target, left, mid - 1)  # discard right half


# print(binary_search_recur(numbers, 67, 0, len(numbers) - 1))


def linear_search(nums: list[int], target) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return None


print(
    timeit.timeit(
        f"binary_search({range(1000)}, {999})",
        setup="""from __main__ import binary_search""",
        number=100000
    )
)
