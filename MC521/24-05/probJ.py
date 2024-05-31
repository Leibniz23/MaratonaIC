def w(u:tuple, v:tuple)->int:
    dist = abs(u[0] - v[0]) + abs(u[1] - v[1])
    return dist

def dfs_visit(g, color, v, t, n, resp):
    if v == t:
         resp[0] = "happy"
         return
    color[v] = 1
    for i in range(1, n):
        u = g[v][i]
        if color[i] == 0 and u <= 1000:
            dfs_visit(g, color, i, t, n, resp)
            if resp[0] == "happy":
                 return
    color[v] = 2

def dfs(g):
    n = len(g)
    color = []
    for i in range(n):
        color.append(0)
    color.append(0)
    resp = ["sad"]
    for i in range(1, n):
        if resp[0] == "happy":
            break
        if g[0][i] <= 1000:
            dfs_visit(g, color, i, len(g)-1, n, resp)
            
        for i in range(1, n):
            color[i] = 0
            
    return resp

def main():
    c = int(input())
    for _ in range(c):
        n = int(input())
        s = tuple(map(int, input().split()))
        stores = []
        stores.append(s)
        for i in range(n):
            stores.append(tuple(map(int, input().split())))
        t = tuple(map(int, input().split()))
        stores.append(t)
        g = []
        for i in range(n+2):
            g.append([])
            for j in range(n+2):
                g[i].append(w(stores[i], stores[j]))
                
        result = dfs(g)
        print(result[0])
            
main()