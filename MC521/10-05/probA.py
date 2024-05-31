def dfs_mod(n, p):
    result = []
    for v in range(n):
        visit = [False for _ in range(n)]
        visit[v] = True
        u = p[v] - 1
        while visit[u] == False:
            visit[u] = True
            u = p[u] - 1
        
        result.append(u+1)   
    return result
        
def main():
    n = int(input())
    p = list(map(int, input().split()))
    
    result = dfs_mod(n, p)
    # Printing
    for i in range(n-1):
        print(result[i], end=" ")
    print(result[n-1])
    
main()