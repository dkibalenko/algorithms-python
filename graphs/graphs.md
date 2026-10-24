
## ⭐ What Is a Graph?

A **graph** is a data structure consisting of:

- **Vertices (nodes)** — entities
- **Edges** — relationships between entities

Formally:

$$G=(V,E)$$

Graphs are **far more flexible than trees** because:

- Nodes can have **any number of connections**
- Cycles are allowed
- They don’t need a root
- They can represent almost any real-world relationship


## ⭐ Why Graphs Matter for Backend Developers

Graphs model:

- Social networks (friends, followers)
- Microservice dependency graphs
- Routing (network packets, GPS)
- Job scheduling (DAGs)
- Recommendation systems
- Database query planners
- State machines
- Knowledge graphs


## ⭐ Graph Types

### 1. Directed vs Undirected Graphs

#### Undirected Graph

Edges have **no direction**.
```
A — B — C
```
**Meaning: A is connected to B, and B is connected to A.**

**Used for**:
- **Social networks** (friendship)
- **Undirected** roads

#### Directed Graph (Digraph)

Edges **have direction**.
```
A → B → C
```
**Used for**:
- Following on Twitter
- Web links
- Task dependencies

---

### 2. Weighted vs Unweighted Graphs

#### Weighted Graph

Edges **have a cost/weight**.
```
A --5--> B --2--> C
```
**Used for**:
- Shortest path (Dijkstra)
- Network routing
- Maps (distance/time)

#### Unweighted Graph

All edges **have equal cost**.

**Used for**:
- BFS shortest path
- Connectivity problems

---

### 3. Cyclic vs Acyclic Graphs

#### Cyclic

Contains **at least one cycle**.
```
A → B → C → A
```

#### Acyclic

**No cycles**.

Most important subtype:

#### **DAG — Directed Acyclic Graph**
```
A → B → D
 \→ C →/
```
**Used for**:
- Job scheduling
- Build systems (Make, Bazel)
- Airflow DAGs
- Git commit history

---

### 4. Connected vs Disconnected Graphs

#### Connected Graph

Every node is reachable.

#### Disconnected Graph

Contains **isolated components**.

**Used for**:
- Clustering
- Community detection

---

### 5. Dense vs Sparse Graphs

#### Sparse

**Few edges** $∣E∣\space≈\space∣V∣$

#### Dense

**Many edges** $∣E∣\space≈\space∣V∣^2$

This affects which adjacency representation you choose.


## ⭐ Graph Representations (Critical for Interviews)

### 1. Adjacency List (Most Common)

```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
```
- Space: $O(V+E)$
- Best for sparse graphs

The **index is the node** and the **value is node's neighbors**.

### 2. Adjacency Matrix
```
    A B C D
A [ 0 0 1 0 ]
B [ 0 0 1 1 ]
C [ 1 1 0 1 ]
D [ 0 1 1 0 ]
```
- Space: $O(V2)$
- Best for **dense graphs**
- **Constant‑time** edge lookup

Zero or one indicates whether the **node X** **has a connection** to node Y.

```python
graph = {
    0: [0, 0, 1, 0],  # node(index) 0 -> 2
    1: [0, 0, 1, 1],  # node(index) 1 -> 2, 3
    2: [1, 1, 0, 1],  # node(index) 2 -> 0, 1, 3
    3: [0, 1, 1, 0]   # node(index) 3 -> 1, 2
}
```

### 3. Edge List
```python
[(A, B), (A, C), (B, D), (C, D)]
```
**Used for**:
- Sorting edges (Kruskal’s MST)


## ⭐ Graph Implementation


### Adjacency List

`node → list of neighbors`

For example, this graph:
```
A ── B ── C
│    │
└── D ── E
```
Can be represented as:
```
{
    "A": ["B", "D"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B", "E"],
    "E": ["D"]
}
```

### Undirected graph

```python
class Graph:
    def __init__(self):
        self.adj = {}  # adjacency list

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, v1, v2):
        # undirected graph
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    def __repr__(self):
        return "\n".join(f"{v}: {nbrs}" for v, nbrs in self.adj.items())
        
# Using the Graph
g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("B", "D")
g.add_edge("D", "E")

print(g)
```
```
A: ['B', 'D']
B: ['A', 'C', 'D']
D: ['A', 'B', 'E']
C: ['B'] E: ['D']
```
