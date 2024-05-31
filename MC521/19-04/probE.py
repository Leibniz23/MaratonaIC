def inversionsIn(lista, n):
    i, count = 0, 0
    while i < n - 1:
        if lista[i] > lista[i+1]:
            count += 1
            i += 1
        i += 1

    return count
        
def main():
    N = int(input())
    for _ in range(N):
        n = int(input())
        lista = list(map(int, input().split()))
        result = inversionsIn(lista, n)
        print(str(result))
    
main()