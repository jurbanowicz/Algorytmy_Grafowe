from dimacs import *
from runtests import run_weighted_graphs

def change_to_adj_directed(Edges, V):
    G = [[] for _ in range(V)]

    for u, v, w in Edges:
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, 0))

    return G
def find_parent(G, u, v):
    for i, x in enumerate(G[u]):
        if x[0] == v:
            return i

def bfs(G, start, end):
    pass


def ford_fulkerson(G, start, end):
    flow = 0
    while (curr_flow := bfs(G, start, end)) > 0:
        flow += curr_flow

    return flow

def main(V, L):
    G = change_to_adj_directed(L, V)
    n = len(G)
    result = ford_fulkerson(G, 0, n - 1)
    return result

if __name__ == "__main__":
    folder_path = "/Users/jacekurbanowicz/Desktop/WIET/Grafowe/Lab_2/graphs-lab2/flow/"
    # graph = "simple"
    # V, L = loadDirectedWeightedGraph(folder_path + graph)
    # print(main(V, L))
    # print("Correct reuslt: ", readSolution(folder_path + graph))
    run_weighted_graphs(folder_path, main)