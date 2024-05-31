INF = 10**10

def bellmanford(g, n):
    dist = [INF] * n
    dist[0] = 0
    for _ in range(n):
        for v in range(n):
            for adj in g[v]:
                u, w = adj
                if dist[u] > dist[v] + w:
                    dist[u] = dist[v] + w
    
    for v in range(n):
            for adj in g[v]:
                u, w = adj
                if dist[u] > dist[v] + w:
                    return "possible"
    
    return "not possible"
        
                
def main():
    n = int(input())
    for _ in range(n):
        n, m = list(map(int, input().split()))
        g = [[] for i in range(n)]
        for i in range(m):
            x, y, t = list(map(int, input().split()))
            g[x].append((y,t))
        possibility = bellmanford(g, n)
        print(possibility)
        
        
main()