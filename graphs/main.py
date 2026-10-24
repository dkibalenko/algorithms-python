class Graph:
    def __init__(self):
        self.adj = {}  # e.g. {"A": ["B", "C"], "B": ["A"], "C": ["A"]}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []  # initialize a neighbour container

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)  # for directed graphs, remove one direction

        self.adj[v1].append(v2)
        self.adj[v2].append(v1)

    def __repr__(self):
        return "\n".join(f"{vtx}: {nbrs}" for vtx, nbrs in self.adj.items())

g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("B", "D")
g.add_edge("D", "E")

print(g)
