from dimacs import *
import sys
from runtests import run_all_graphs
sys.setrecursionlimit(100000)

def change_to_adj(Edges, V):
    G = [[] for _ in range(V)]

    for u, v, w in Edges:
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    return G

def dfs(G, start, end, min_w):
    n = len(G)
    vis = [False] * n


    dfs_visit(G, start, vis, min_w)

    return vis[end]

def dfs_visit(G, v, vis, min_w):
    vis[v] = True

    for u, w in G[v]:
        if not vis[u] and w >= min_w:
            dfs_visit(G, u, vis, min_w)

def bin_search(Weights, G, start, end):
    n = len(Weights)

    r = n - 1
    l = 0

    while r - l > 1:
        m = (r + l) // 2
        if dfs(G, start, end, Weights[m]):
            r = m
        else:
            l = m + 1

    return Weights[r]


def solution(V, L):
    G = change_to_adj(L, V)

    W = [0 for _ in range(len(L))]

    for i, x in enumerate(L):
        W[i] = x[2]

    W.sort(reverse=True)
    return bin_search(W, G, 0, 1)



if __name__ == "__main__":

    graphs_folder = "/Users/jacekurbanowicz/Desktop/WIET/Grafowe/Lab_1/graphs-lab1/"
    run_all_graphs(graphs_folder, solution)