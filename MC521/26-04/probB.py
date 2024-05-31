def main():
    n, x = map(int, input().split())
    vector = list(map(int, input().split()))
    count, soma, ini = 0, 0, 0

    for i in range(n):
        soma += vector[i] # Coloca os elementos do final na soma
        
        while soma > x and ini <= i: # Vai eliminando os elementos do inicio até ser <= x
            soma -= vector[ini]
            ini += 1
        
        if soma == x:
            count += 1

    print(str(count))
    
main()