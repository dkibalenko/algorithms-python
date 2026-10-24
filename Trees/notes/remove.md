## The three valid BST deletion cases

### Case 1 — Node has NO right child
Replace the node with its left child.

### Case 2 — Node has a right child, but that right child has NO left child
Replace the node with its right child, and attach the node’s left subtree under it.

### Case 3 — Node has a right child WITH a left child
Find the leftmost node in the right subtree (the inorder successor), move it up, and reattach children.
