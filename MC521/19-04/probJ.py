def sum_char(num:str) -> int:
    # Devolve a soma dos algarismos que compoem num
    ret = 0
    for char in num:
        ret += int(char)
        
    return ret

def soma(n:int, casos:list) -> int:
    if n < len(casos):
        return casos[n]
    
    for i in range(2, n+1):
        atual = casos[i-1] + sum_char(str(i))
        casos.append(atual)
    
    return casos[n]

def main():
    t = int(input())
    entradas = []
    casos = [0,1]
    largest = 0
    for case in range(t):
        n = int(input())
        entradas.append(n)
        if n > largest:
            largest = n
    
    soma(largest, casos)
    for i in entradas:
        print(str(soma(i, casos)))
    
    
main()