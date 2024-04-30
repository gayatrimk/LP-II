import sys

class Graph:
    def __init__(self):
        self.V = 0
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])
        self.V = max(self.V, u, v) + 1

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = None
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True
            for v in range(self.V):
                if any(edge[0] == u and edge[1] == v or edge[1] == u and edge[0] == v for edge in self.graph):
                    if not mst_set[v] and key[v] > self.graph[u][2]:
                        key[v] = self.graph[u][2]
                        parent[v] = u

        print("Edges in the Minimum Spanning Tree:")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} : {key[i]}")

        total_cost = sum(key)
        print(f"\nMinimum Cost of MST: {total_cost}")

# Get user input for the graph
g = Graph()
m = int(input("Enter the number of edges: "))
for _ in range(m):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    g.add_edge(u, v, w)

g.prim_mst()