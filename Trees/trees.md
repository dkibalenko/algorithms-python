[Docs](https://takeuforward.org/binary-tree/introduction-to-trees/)

[W3School](https://www.w3schools.com/dsa/dsa_theory_trees.php)
# ⭐ Trees Introduction


A **Tree** is a **hierarchical data structure** made up of **nodes** connected by **edges**.

- The **topmost node** is called the **root**.
- Each node can have **zero or more children(left & right one)**.
- Nodes with **no children** are called **leaves**.
- Every node (except the root) has exactly **one parent**.
- There are **no cycles** (unlike graphs).

Think of it like an **inverted family tree**: root at the top, children branching downward.

---

## 📖 Key Terminology

- **Root**: The starting node (e.g., $C:$ in Windows file system).
- **Parent**: A node that has children.
- **Child**: A node directly connected below a parent.
- **Leaf**: A node with **no children**.
- **Siblings**: Nodes with the **same parent.**
- **Edge**: A **link** connecting one node to another.
- **Depth of a node**: The **number of edges ==from the root** to a **given node==**. (Root -> Node). The root node has depth **zero**. [Link](https://en.wikipedia.org/wiki/Tree_(abstract_data_type))
- **Height of a node**: The **largest number of edges** in a path **from that node to a leaf**. (Node -> Leaf). Leaf nodes have height zero.
	- A **leaf** has height **0**.
	- Its parent has height **1**.
	- A tree with only a single node (hence both a root and leaf) has depth & height **zero**
	```
							5
						/       \
					   /         \
					  10           15
					/    \       /    \
				  /       \    /        \
				 20       25  30         35
				            \
				             \
				             45
	```
	- Depth of node 10 = 1 (number of edges in the path from root node to the node)
	- Height of node 10 = 2 (number of edges in the longest path connecting the node & any leaf)
- **Tree Height**: The **height of the root** node.
	- Height of a tree with only one node (root node) is 0
	- The **depth** of a whole binary tree, is **equivalent** to the height of the binary tree
- **Subtree**: Any node and all its descendants.
- **Tree size**: The number of nodes in the tree.

---

## 🌲 Why height is defined from the bottom

This definition makes many tree formulas elegant and consistent:

- Height of a **leaf** = 0
- A **perfect tree** of height $h$ has $h+1$ levels
- Number of nodes in a perfect tree:
$$2^{h+1}−1$$
- Number of leaves:
$$2^h$$
If height were measured from the root, these formulas would break or become inconsistent.

---

## 🧩 Types of Trees

- **General Tree**: Any number of children per node.
- **Binary Tree**: Each node has **at most two children** (left & right).
- **Binary Search Tree (BST)**: Left child $<$ Parent $<$ Right child.
- **AVL / Red-Black Trees**: Self-balancing BSTs for efficient operations.
- **B-Trees**: Used in databases and filesystems for fast disk access.
- **Heaps**: Specialized trees for priority queues.

---

## ⚡ Why Trees Matter

- **File Systems**: Directories and files form a tree.
- **Databases**: Indexing (B-Trees, B+ Trees).
- **Compilers**: Abstract Syntax Trees (ASTs).
- **Networking**: Routing tables.
- **AI/ML**: Decision Trees.

---

## 🔎 Visual Example (Binary Tree)


```
        A (root)
       / \
      B   C
     / \   \
    D   E   F
```

- Root = A
- Children of A = {B, C}
- Leaves = {D, E, F}
- Height = 2

---

**Key Takeaways**

1. **Hierarchical Structure**: Trees differ from linear data structures like arrays and linked lists because they have a hierarchical format. They consist of a root node and multiple child nodes.

2. **Parent-Child Relationships**: Each node in a tree can have **one parent** and **multiple children**, establishing a clear hierarchical relationship.

3. **Leaf Nodes**: Leaf nodes are the endpoints of the tree, representing **nodes that do not have any children**.

4. **Practical Applications**: Trees are widely used in technology, including the Document Object Model (DOM) in web pages, chess algorithms, Facebook comment threads, and [abstract syntax trees](https://en.wikipedia.org/wiki/Abstract_syntax_tree) in programming.

5. **Comparison with Linked Lists**: While linked lists can be viewed as a **single-path tree**, trees allow multiple branches and paths, providing more flexibility.

6. **Variety of Trees**: There are many types of tree data structures, but it's advised not to feel overwhelmed. Focus on the main types that are commonly encountered in interviews and practical scenarios.

---

# ⭐ Binary Tree

1. Each parent node can only have either **zero**, **one** or **two child nodes**
2. Each child can only have **one parent**.
3. Each node represents a certain state.

## 🌲 Main Types of Binary Trees

Here are the most common [categories](https://takeuforward.org/binary-tree/introduction-to-trees) you’ll encounter:

### 1. Full Binary Tree(0 or 2 children)

- Every node has **==either 0 or 2 children==**.
- Example:
```
		A
	   / \
	  B   C
	/   \
   D     E
```

### 2. Complete Binary Tree(0-1-2 children)

- **All levels are completely filled** except possibly the **last**, which is can also be full, or filled from ==**left to right**==.
- The properties of a complete Binary Tree means it is **also balanced.**
- Used in **heaps**.
```
         A
       /   \
      B     C
     / \   /
    D   E F
```

If you want to include G, it must be placed **after F**, like this:
```
         A
       /   \
      B     C
     / \   / \
    D   E F   G
```
This is still complete — and now also **perfect**.

### 3. Perfect Binary Tree

- **All internal nodes** have exactly **two children**.
- **All leaf nodes** are at the **same depth** (i.e., same level).
- ==The **number of leaves** is **exactly**== $2^h$ ($h$ - the height of the tree) **or** is equal to the **sum of all nodes above it plus one**.
- ==The **total number of nodes**== in a perfect binary tree of height $h$ is:
$$\text{Total nodes} = 2^{h+1}-1$$
- It's **very efficient** and is desirable.
- [Example](<file:///D:/EDUCATION\ALGORITHMS & DATA STRUCTURES/Binary Trees/Perfect binary tree.png>)
```
        A
       / \
      B   C
     / \  / \
    D   E F  G
```

### 4. Balanced Binary Tree(AVL [Tree](https://medium.com/basecs/the-little-avl-tree-that-could-86a3cae410c7), Red-Black [Tree](https://medium.com/basecs/painting-nodes-black-with-red-black-trees-60eacb2be9a5))
- Has the **heights of the two subtrees of any node differ by at most one**.
- This property ensures that the tree remains **relatively well-balanced**, preventing the tree from becoming highly skewed or degenerate.
- Examples: **AVL [Tree](https://visualgo.net/en/bst), Red-Black [Tree](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)**.
```
        A
       / \
      B   C
     / \
    D   E
```

### 5. Degenerate (Skewed) Binary Tree
- **Each parent has only one child** → **behaves like a linked list**.
- Worst case for BST if unbalanced.

---

## ⚡ Time Complexity of Operations

Let’s compare the main binary tree variants:

| Tree Type                       | Lookup                                       | Insert            | Delete            | Notes                                                     |
| ------------------------------- | -------------------------------------------- | ----------------- | ----------------- | --------------------------------------------------------- |
| **Binary Tree (unstructured)**  | $O(n)$                                       | $O(n)$            | $O(n)$            | **No ordering**; must traverse nodes.                     |
| **Binary Search Tree (BST)**    | $O(n$) → $O(log\space  n)$ avg, $O(n$) worst | $O(h)$            | $O(h)$            | Depends on height `h`. Skewed BST = $O(n)$.               |
| **AVL Tree (Balanced BST)**     | $O(log\space  n)$                            | $O(log\space  n)$ | $O(log\space  n)$ | **Strictly balanced** → guarantees $log\space n$.         |
| **Red-Black Tree**              | $O(log\space  n)$                            | $O(log\space  n)$ | $O(log\space  n)$ | **Balanced** but less strict than AVL; used in maps/sets. |
| **Heap (Complete Binary Tree)** | $O(n)$ for search                            | $O(log\space  n)$ | $O(log\space  n)$ | Optimized for min/max retrieval, not general search.      |

## 🔑 Key Takeaways

- **Unstructured binary trees** are inefficient ($O(n)$).
- **BSTs** are efficient ==**only if balanced**==.
- **AVL/Red-Black Trees** ==guarantee logarithmic performance==.
- **Heaps** are specialized for priority queues, not searching.

---

## $O (log_{base}\space (n))$ - $n$ is divided by $base$

Video [Explanation](https://www.youtube.com/watch?v=M4ubFru2O80)
[Docs](https://takeuforward.org/binary-tree/introduction-to-trees/)
### CS uses base 2
$$log_2\space (8) = 3;\space\space2^3 = 8\space\space(\text{8 ➡️ 4 ➡️ 2 ➡️ 1})$$
### Math(Calculus) uses base 10:
$$log_{10}\space (100) = 2;\space\space10^2 = 100$$
---

# ⭐ Binary Search Tree

[Docs](https://takeuforward.org/binary-search-tree/introduction-to-binary-search-trees/)
Visualization is [here](https://visualgo.net/en/bst)

A Binary Search Tree is a binary tree where **left < node < right**, allowing fast (logarithmic) search, insert, and delete — unless the tree becomes unbalanced, in which case performance degrades to linear.

A **Binary Search Tree** is a special kind of binary tree where:
- Every node has **at most two children** (left and right)
- **Left subtree contains only values smaller than the node**
- **Right subtree contains only values larger than the node**
- This rule applies **recursively** to every node in the tree

This ordering is what makes searching fast.


---

## Why BSTs Are Fast

Because the tree is **ordered**, every comparison lets you **throw away half of the remaining tree**, just like binary search in a sorted array.

So:
- **Search** ≈ $O(log\space n)$ on average
- **Insert** ≈ $O(log\space n)$ on average
- **Delete** ≈ $O(log\space n)$ on average

But only if the tree is **balanced**.

---

## ❗The Big Caveat: Order of Insertions Matters

If you insert values in a bad order (e.g., sorted input):
```
1 → 2 → 3 → 4 → 5
```
The BST becomes a **linked list**:
```
1
 \
  2
   \
    3
     \
      4
       \
        5
```
This is called a **degenerate tree**, and performance drops to:
- **Search** = $O(n)$
- **Insert** = $O(n)$
- **Delete** = $O(n)$

This is why **self‑balancing BSTs** exist.

---

## Self‑Balancing BSTs (Fixing the Worst Case)

To avoid degeneracy, we use trees that **automatically rebalance**:
- **AVL Tree** (first self‑balancing BST, 1962)
- **Red‑Black Tree**
- **Splay Tree**
- **Treap**
- **B‑Tree** (used in databases)

These guarantee:
- **Worst‑case $O(log\space n)**$ for search, insert, delete
- Tree height stays around **log₂(n)**

---

## Why Use a BST Instead of a Plain Binary Tree?

A plain binary tree has **no ordering rules**, so searching is basically:
- Look everywhere
- Worst case: $O(n)$

A BST uses ==ordering== to **cut the search space in half** at every step.

Example:

Searching for value `30`:
1. Compare with root
2. If 30 > root → go right
3. If 30 < root → go left
4. Repeat until found or subtree is empty

This is **binary search on a tree** → hence the name.

---

## BST Operations (Core Set)

1. **Search** Follow left/right pointers based on comparisons.
2. **Insert** Search for the correct position, then attach a new node.
3. **Delete** Three cases:
    - Node is a leaf
    - Node has one child
    - Node has two children (replace with **inorder successor**)
4. **Traversal**
    - **Inorder** → sorted order
    - Preorder
    - Postorder
    - Level‑order

---

## # **Time Complexity Summary**

| Operation | Average          | Worst  |
| --------- | ---------------- | ------ |
| Search    | $Θ(log\space n)$ | $O(n)$ |
| Insert    | $Θ(log\space n)$ | $O(n)$ |
| Delete    | $Θ(log\space n)$ | $O(n)$ |

Worst case happens when the tree becomes skewed.

---

## Pros

- Better than $O(n)$
- Ordered
- Flexible Size

## Cons

- No $O(1)$ operations

---

# ⭐ Binary Heap

| Lookup     | $O(n)$           |
| ---------- | ---------------- |
| **Insert** | $O(log\space n)$ |
| **Delete** | $O(log\space n)$ |
- ==A **complete binary tree** (every level ALWAYS **filled left‑to‑right**)==
- That satisfies the **heap property**
    - **Min‑heap:** every parent ≤ its children
    - **Max‑heap:** every parent ≥ its children
- No concept of an **unbalanced binary tree**, since there is ALWAYS **left->right** insertion.

Unlike BST, a Binary Heap doesn't care about **left** child to be always less than the **right** child. As long as any child is less than the parent it's ok.

## Min‑Heap
```
        4
       /  \
      7    8
     / \   / \
    9  10 15 20
```
This is a valid **min‑heap** because:
- 4 ≤ 7 and 4 ≤ 8
- 7 ≤ 9 and 7 ≤ 10
- 8 ≤ 15 and 8 ≤ 20

And it is **complete** — filled left‑to‑right with no gaps.

## Array representation (how heaps are stored in memory)

Binary heaps are almost always stored in arrays:
```
Index:  0  1  2  3  4  5   6
Value: [4, 7, 8, 9, 10, 15, 20]
```
**Parent/child relationships**:
- Parent(i) = (i - 1) // 2
- Left(i) = 2*i + 1
- Right(i) = 2*i + 2

Example:
- Node at index 0 → 4
    - Left child: index 1 → 7
    - Right child: index 2 → 8
- Node at index 1 → 7
    - Left child: index 3 → 9
    - Right child: index 4 → 10

## Max‑Heap

Here’s the same structure but as a **max‑heap**:
```
        20
       /  \
     15    10
    / \   / \
   9   7  8   4
```
Binary Heaps are great at doing comparative operations

---

# ⭐ Priority Queue

A **priority queue** is like a normal queue — except **each element has a priority**, and the element with the _highest_ (or _lowest_) priority is **always removed first**.

Not FIFO.
Not LIFO.
But **priority‑driven**.

Think of it as:

> “A queue where the most important item gets served first.”


| Pros               | Cons        |
| ------------------ | ----------- |
| Better than $O(n)$ | Slow lookup |
| Priority           |             |
| Flexible Size      |             |
| Fast Insert        |             |


---

## 🔄 How Priority Queues differ from normal Queues

Here’s the contrast:

|Feature|Queue|Priority Queue|
|---|---|---|
|Order of removal|FIFO (first in, first out)|Based on priority|
|Example behavior|People in line at a store|Emergency room triage|
|Data structure|Usually a linked list or array|Usually a **binary heap**|
|Operations|enqueue, dequeue|insert, extract‑min / extract‑max|

A normal queue doesn’t care about value — only **arrival order**. A priority queue cares _only_ about **priority**.

---

## 🌲 How Priority Queues relate to Binary Heaps

A **binary heap** is the most common way to implement a priority queue efficiently.

Because a binary heap gives:
- **Insert** in $O(log⁡\space n)$
- **Extract‑min / extract‑max** in $O(log⁡\space n)$
- **Peek** in $O(1)$
- **Complete tree structure** stored in an array

This makes heaps perfect for priority queues.

Here’s a min‑heap (used for a min‑priority queue):
```
        4
       / \
      7   8
     / \ / \
    9 10 15 20
```
The smallest element (4) is always at the top — so removing the highest‑priority item is trivial.

---

## 🎯 Real‑world examples of Priority Queues

### **1. Operating system task scheduling**

Processes with higher priority run first.

### **2. Dijkstra’s shortest path algorithm**

Nodes with the smallest tentative distance are extracted first.

### **3. Event simulation systems**

Next event in time is processed first.

### _4. A_ pathfinding*

Nodes with the lowest estimated cost are expanded first.

### **5. Job scheduling in servers**

Urgent tasks jump ahead of routine tasks.

### **6. Huffman coding**

Greedy algorithm repeatedly extracts the two smallest nodes.

---

## 🧠 Why binary heaps are the perfect match

Priority queues _could_ be implemented with:

- Sorted arrays (slow insert)
- Sorted linked lists (slow access)
- Balanced BSTs (more overhead)

But binary heaps hit the sweet spot:

- Fast
- Simple
- Memory‑efficient
- Array‑based (no pointers needed)
- Always complete (no gaps)

This is why almost every language’s standard library uses heaps for priority queues.

---

# ⭐ Trie

A **Trie** (Prefix Tree) is a **tree‑like data structure** used to store strings **character by character**. Each path from the root to a node represents a **prefix**.

Tries allow to know if a word or part of a word exists in a body of text.

It’s perfect for:
- autocomplete
- spell‑checking
- prefix search
- dictionary word storage
- IP routing
- word games (Scrabble, Boggle)

Here’s the key idea:

> Instead of storing whole words in each node, a Trie stores **one character per node**, and words share common prefixes.

---

## 🧩 Visual Example: Storing “cat”, “car”, “dog”

```
        (root)
       /      \
      c        d
     /          \
    a            o
   / \            \
  t   r            g
```
Notice how **cat** and **car** share the prefix **ca**, so the Trie stores it only once.

---

## 🔍 How a Trie differs from a normal tree or hash map

### **Trie vs Hash Map**

| Feature       | Trie                            | Hash Map       |
| ------------- | ------------------------------- | -------------- |
| Lookup        | $O(m)$ where m = length of word | $O(1)$ average |
| Prefix search | Very fast                       | Not supported  |
| Memory        | Higher                          | Lower          |
| Order         | Lexicographical                 | None           |

A Trie is unbeatable for **prefix operations**, but uses more memory.

### **Trie vs Binary Tree**

- Binary trees compare whole values
- Tries compare **characters one by one**
- Tries can have many children (not just 2)

---

## ⚙️ How a Trie works internally

Each node typically contains:

- A dictionary of children
- A boolean flag `is_end_of_word`

Example node structure:
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
```

---

## ✨ Operations

### **1. Insert a word**

Insert “cat”:
- root → c → a → t
- Mark t as end of word

### **2. Search for a word**

Walk character by character:
- If any character is missing → word not found
- If final node has `end=True` → word exists

### **3. Prefix search**

To check if any word starts with “ca”:
- Walk c → a
- If path exists → prefix exists
- No need to check `end`

This is why autocomplete is so fast.

---

## 🎯 Real‑world examples of Tries

### **Autocomplete**

Type “app” → instantly find “apple”, “application”, “apply”.

### **Spell check**

Find nearest words by exploring neighbors.

### **Search engines**

Prefix indexing for fast suggestions.

### **IP routing**

Compressed tries (radix trees) store routing prefixes.

### **Word games**

Efficiently check valid words and prefixes.
