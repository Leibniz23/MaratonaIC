def calcular(pontos, x):
    for ponto in pontos:
        m = -(ponto[1]/(ponto[0]+1))
        n = -(ponto[1]/(ponto[0]-1))
        acima_m, acima_n = 0, 0
        for cherry in pontos:
            if (cherry[1])/(cherry[0]) > m:
                acima_m+= 1
            elif (cherry[1])/(cherry[0]) > n:
                acima_n+=1

        if (acima_m) == x:
            return str(ponto[0]+1), str(ponto[1])
        elif (acima_n) == x:
            return str(ponto[0]-1), str(ponto[1])

def main():
    n = int(input())
    while n != 0:
        pontos = []
        for _ in range(2*n):
            i, j = input().split()
            i, j = int(i), int(j)
            pontos.append((i,j))
        a, b = calcular(pontos)
        print(a + " " + b)
        n = int(input())
    
    


main()