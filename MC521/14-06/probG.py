import math

def bpm(graph, i, matchR, seen):
    for v in range(len(graph[i])):
        if graph[i][v] and seen[v] == False:
            seen[v] = True
            if matchR[v] == -1 or bpm(graph, matchR[v], matchR, seen):
                matchR[v] = i
                return True
    return False
 
def maxBPM(graph):    
    matchR = [-1] * len(graph[0])
    result = 0
    for i in range(len(graph)):
        seen = [False] * len(graph[0])
        if bpm(graph, i, matchR, seen):
            result += 1
    return result

def dist(a:list, b:list)-> float:
    result = ((a[0] - b[0])**2 + (a[1] - b[1])**2)
    result = math.sqrt(result)
    return result

def main():
    while True:
        try:
            n, m, s, v = list(map(int, input().split()))
        except EOFError:
            break

        g = []
        max_dist = s*v
        gopher = []
        holes = []
        for _ in range(n):
            gopher.append(list(map(float, input().split())))
        for _ in range(m):
            holes.append(list(map(float, input().split())))
            
        for i in range(n):
            g.append([])
            for j in range(m):
                distance = dist(gopher[i], holes[j])
                if distance <= max_dist:
                    g[i].append(1)
                else:
                    g[i].append(0)
                    
        complement = maxBPM(g)
        print(str(n - complement))
        
                
main()