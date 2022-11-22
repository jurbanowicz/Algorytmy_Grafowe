from dimacs import *
from runtests import *


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

def dfs(G, start, end):
    n = len(G)
    min_w = float('inf')
    st = []
    vis = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    parent[start] = start
    st.append(start)
    while st:
        u = st.pop()
        vis[u] = True
        if u == end:
            break
        for v, w in G[u]:
            if not vis[v] and w > 0:
                st.append(v)
                parent[v] = u
                min_w = min(min_w, w)

    if vis[end]:
        curr = end
        while curr != start:
            p = find_parent(G, curr, parent[curr])
            c = find_parent(G, parent[curr], curr)
            G[curr][p] = (G[curr][p][0], G[curr][p][1] + min_w)
            G[parent[curr]][c] = (G[parent[curr]][c][0], G[parent[curr]][c][1] - min_w)
            
            curr = parent[curr]
        return min_w
    return 0



def ford_fulkerson(G, start, end):
    flow = 0
    while (curr_flow := dfs(G, start, end)) > 0:
        flow += curr_flow
    return flow

def copy_graph(G):
    n = len(G)
    X = []
    for item in G:
        X.append(item)
    return X


def main(V, L):
    G = change_to_adj_directed(L, V)

    n = len(G)
    result = []
    for i in range(1, n):
        g_1 = copy_graph(G)
        result.append(ford_fulkerson(g_1, 0, i))
    return sum(result)

if __name__ == "__main__":
    folder_path = "/Users/jacekurbanowicz/Desktop/WIET/Grafowe/Lab_2/graphs-lab2/connectivity/"
    graph = "rand100_500"
    print("Correct result: ", readSolution(folder_path + graph))
    V, L = loadWeightedGraph(folder_path + graph)
    print(main(V, L))
    # run_weighted_graphs(folder_path, main)
