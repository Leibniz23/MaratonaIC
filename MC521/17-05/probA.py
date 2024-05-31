import heapq

INF = 10**10

def dijkstra(g, s):
    # Init
    n = len(g)
    dist = [INF for i in range(n)]
    heap = []
    dist[s] = 0
    heapq.heappush(heap, [0, s])
    #
    while len(heap) > 0:
        key, v = heapq.heappop(heap)
        for adj in g[v]:
            u, w = adj
            if dist[u] > dist[v] + w:
                dist[u] = dist[v] + w
                heapq.heappush(heap, [dist[u], u])
    return dist

def main():
    n = int(input())
    count = 1
    for _ in range(n):
        vertex, edges, s, t = list(map(int, input().split()))
        g = [[] for i in range(vertex)]
        for i in range(edges):
            u, v, w = list(map(int, input().split()))
            g[u].append((v,w))
            g[v].append((u,w))
        dist = dijkstra(g,s)
        result = dist[t]
        if result >= INF:
            print("Case #" + str(count) + ": unreachable")
        else:
            print("Case #" + str(count) + ": " + str(result))
        count += 1
            
main()

