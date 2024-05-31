def soma_memoizada(planks, k) -> int: # retorna o ini da maior soma encontrada
    soma = []
    soma.append(sum(planks[0:k])) # primeira soma, até k-1
    ini, best_i, best_val, fim = 1, 0, soma[0], k
    len_p = 1
    while fim < len(planks):
        atual = soma[len_p-1] - planks[ini-1] + planks[fim]
        soma.append(atual)
        if atual < best_val:
            best_val = atual
            best_i = ini
        len_p += 1
        ini += 1
        fim += 1
        
    return best_i + 1 # corrigindo o indice
    

def main():
    n, k = map(int, input().split())
    planks = list(map(int, input().split()))
    result = soma_memoizada(planks, k)
    print(str(result))

main()