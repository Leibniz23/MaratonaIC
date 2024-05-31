def dfs_visit(g, color, v):
    i = 0
    color[v] = 1
    adj_v = g[v]
    while i <= len(adj_v) - 1:
        u = adj_v[i]
        if color[u] == 0:
            dfs_visit(g, color, u)
        i += 1
    color[v] = 2

def count_components(g):
    # Baseado em DFS
    color = [0 for i in range(len(g))]
    count = 0
    for v in range(len(g)):
        if color[v] == 0:
            count += 1
            dfs_visit(g, color, v)
            
    return count
            
def set_edges(g, r):
    for _ in range(r):
        u, v = list(map(int, input().split()))
        g[u].append(v)
        g[v].append(u)

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        r = int(input())
        g = [[] for i in range(m)] # Lista de adjacencias
        set_edges(g, r)
        t = count_components(g)
        if t <= 1:
            print("0")
        else:
            print(str(t-1))
            
main()
        