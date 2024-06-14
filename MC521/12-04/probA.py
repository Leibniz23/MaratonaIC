# def knapSack(W, vetw, vetc, n, z): # Recursivo não passou no tempo
#     if z[n][W] > -1: # Caso já resolvido
#         return z[n][W]
    
#     if n==0 or W == 0: # Casos de borda
#         z[n][W] = 0
#         return 0
    
#     if vetw[n-1] > W: # Se a mochila já está cheia só repete maximo valor anterior conhecido
#         z[n][W] = knapSack(W, vetw, vetc, n-1, z)
#     else: # Melhor entre colocar o item e não colocar ele
#         z[n][W] = max(knapSack(W, vetw, vetc, n-1, z), vetc[n-1] + knapSack(W-vetw[n-1], vetw, vetc, n-1, z))
    
#     return z[n][W]

def knapSack(W, vetw, vetc, n, z):
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0: # Casos de borda
                z[i][j] = 0
            elif vetw[i-1] > j: # Se a mochila já está cheia só repete maximo valor anterior conhecido
                z[i][j] = z[i-1][j]
            else: # Caso geral
                z[i][j] = max(z[i-1][j], vetc[i-1] + z[i-1][j - vetw[i-1]])

    return z[n][W]


def main():
    s, n = map(int, input().split())
    vetw, vetc = [], []
    for _ in range(n):
        w, c = map(int, input(). split())
        vetw.append(w)
        vetc.append(c)

    z = [[-1]*(s+1) for _ in range(n+1)]
    print(str(knapSack(s, vetw, vetc, n, z)))

main()