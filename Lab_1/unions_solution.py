from runtests import run_all_graphs
from collections import deque
# from dimacs import loadWeightedGraph
# from dimacs import readSolution
class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices # number of vertices in the graph
        self.edges = [] # graph edges list, tuple (w - weight of the edge, u - start vertex, v - end vertex)
        self.graph = [[] for _ in range(self.V)] # adjecency list for dfs

    def add_edge(self, u, v, w):
        self.edges.append((w, u, v))
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dfs(self): # returns if path between vertecies 0 and 1 exists
        vis = [False for _ in range(self.V)]

        st = deque()
        st.append(0)
        while st:
            u= st.pop()
            vis[u] = True
            if u == 1:
                return True
            for v, w in self.graph[u]:
                if not vis[v]:
                    st.append(v)

        return vis[1]

    def find(self, parent, v):
        if parent[v] == v:
            return v
        else:
            return self.find(parent, parent[v])

    def union(self, parent, u, v):
        parent[u] = v

    def main(self, edge_list): # edge list of the full graph (u, v, w)
        edge_list.sort(key = lambda x: x[2], reverse = True)
        parent = [i for i in range(self.V)] # set parent of each vertex as self

        for u, v, w in edge_list:
            u -= 1
            v -= 1
            self.union(parent, self.find(parent, u), self.find(parent, v))
            self.add_edge(u, v, w)
            if self.find(parent, 0) == self.find(parent, 1):
                return w

def solution(V, L):
    G = Graph(V)
    result = G.main(L)
    return result

if __name__ == "__main__":
    graphs_folder = "/Users/jacekurbanowicz/Desktop/WIET/Grafowe/Lab_1/graphs-lab1/"
 
    # file_name = "g1"
    # (V,L) = loadWeightedGraph(graphs_folder + file_name)
    # print(solution(V, L))
    # print("Expected result: " , readSolution(graphs_folder + file_name))

    run_all_graphs(graphs_folder, solution)