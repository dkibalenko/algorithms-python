### ✅ Step 1 — Handle empty tree
```py
if not self.root:
    return None
```
If the tree has no nodes, there’s nothing to find.

### ✅ Step 2 — Start at the root
```py
current_node = self.root
```
All BST searches begin at the root.

### ✅ Step 3 — Traverse down the tree
You compare the target value with the current node:
#### If the value is smaller → go left
```py
if value < current_node.value:
    current_node = current_node.left
```
#### If the value is larger → go right
```py
elif value > current_node.value:
    current_node = current_node.right
```
#### If equal → found it
```py
else:
    return current_node
```

### 🧠 Why this works
Because your `insert()` method maintains **the binary search tree invariant**:
- **Left subtree** contains values **smaller** than the node
- **Right subtree** contains values **greater** than the node

So lookup can eliminate **half the tree at each step** — exactly like **binary search**.