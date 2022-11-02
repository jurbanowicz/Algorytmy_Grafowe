from queue import PriorityQueue
from runtests import run_all_graphs
from dimacs import loadWeightedGraph

def change_to_adj(Edges, V):
    G = [[] for _ in range(V)]

    for u, v, w in Edges:
        u -= 1
        v -= 1
        w *= -1
        G[u].append((v, w))
        G[v].append((u, w))

    return G

def find_weight(G, u, v):
    for x, w in G[u]:
        if x == v:
            return w

def dijkstra(G):
    n = len(G)
    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    vis = [False for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    d[0] = 0
    Q.put((0, 0))


    while not Q.empty():
        _, u = Q.get()
        vis[u] = True
        if u == 1:
            break
        for v, w in G[u]:
            if not vis[v]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    parent[v] = u
                    Q.put((d[v], v))


    curr_v = 1
    max_w = -1*float('inf')
    while curr_v != 0:
        curr_w = find_weight(G, curr_v, parent[curr_v])
        if curr_w > max_w:
            max_w = curr_w
        curr_v = parent[curr_v]

    return max_w

def solution(V, L):
    G = change_to_adj(L, V)
    result = -1*dijkstra(G)
    return result

if __name__ == "__main__":
    graphs_folder = "/Users/jacekurbanowicz/Desktop/WIET/Grafowe/Lab_1/graphs-lab1/"

    # V, L = loadWeightedGraph(graphs_folder + "g1")
    # print(solution(V, L))


    run_all_graphs(graphs_folder, solution)

