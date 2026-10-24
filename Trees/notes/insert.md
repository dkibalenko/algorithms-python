# 🌳 How your insert() method works

The method builds the BST by walking down the tree until it **finds the correct empty spot**.

## 1. Create a new node
```py
new_node = Node(value)
```
## 2. If the tree is empty, the new node becomes the root
```py
if self.root is None:
    self.root = new_node
```
## 3. Otherwise, walk down the tree
```py
current_node = self.root
```
## 4. Compare the value with the current node
- If `value < current_node.value`, go **left**
- Otherwise, go **right**

This is the BST invariant.

## 5. If the child spot is empty, insert the node there
Example:
```py
if current_node.left is None:
    current_node.left = new_node
    return self
```

## 6. If not empty, keep walking down the tree
```py
current_node = current_node.left
```
This repeats until the correct position is found.

## 🌲 How the tree grows with your insert calls
You insert values in this order:
```
9, 4, 6, 20, 170, 15, 1
```
Let’s walk through the structure:

### Insert 9
Tree is empty → 9 becomes root.

### Insert 4
- 4 < 9 → goes left.

### Insert 6
- 6 < 9 → go left
- 6 > 4 → go right

### Insert 20
- 20 > 9 → go right

### Insert 170
- 170 > 9 → right
- 170 > 20 → right

### Insert 15
- 15 > 9 → right
- 15 < 20 → left

### Insert 1
- 1 < 9 → left
- 1 < 4 → left

You end up with:
```
        9
    4       20
  1   6   15   170
```

## 🧩 How `traverse()` visualizes the tree
Your Python version:
```py
def traverse(node):
    if node is None:
        return None

    tree = {"value": node.value}
    tree["left"] = traverse(node.left)
    tree["right"] = traverse(node.right)
    return tree
```
What it does:
- Starts at the root
- Creates a dict: `{ "value": node.value }`
- Recursively builds `"left"` and `"right"`
- Returns a nested dictionary representing the whole tree

```py
{
  "value": 9,
  "left": {
    "value": 4,
    "left": {"value": 1, "left": None, "right": None},
    "right": {"value": 6, "left": None, "right": None}
  },
  "right": {
    "value": 20,
    "left": {"value": 15, "left": None, "right": None},
    "right": {"value": 170, "left": None, "right": None}
  }
}
```
## 🔍 Why `insert()` + `traverse()` work well together
- `insert()` builds the BST structure in memory.
- `traverse()` walks that structure and converts it into a JSON‑friendly nested dictionary.

This makes it easy to debug, visualize, or export the tree.
