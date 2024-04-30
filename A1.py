from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        self.dfs_util(start, visited)
        print()

    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print()

def main():
    g = Graph()

    # Adding edges to the graph
    g.add_edge(1,3)
    g.add_edge(1,7)
    g.add_edge(3,2)
    g.add_edge(3,4)
    g.add_edge(7,8)
    g.add_edge(4,8)
   

    print("DFS traversal:")
    g.dfs(1)

    print("BFS traversal:")
    g.bfs(1)

if __name__ == "__main__":
    main()
