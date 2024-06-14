MOD = 10**9 + 7

def comb(n, vet):
    if n <= vet[0]:
        return vet[n]

    for i in range(vet[0]+1, n+1): # não conhece fib(n)
        vet[i] = (vet[i-1] + vet[i-2]) % MOD

    vet[0] = i # o ultimo conhecido é fib(n)
    return vet[n]

def main():
    string = input()
    possiveis = 1
    i = 0
    vet = [0 for _ in range(len(string)+1)]
    vet[0], vet[1], vet[2] = 2, 1, 2
    while i < len(string) - 1:
        count = 0
        if string[i] == 'u':
            count +=1
            while i < len(string)-1 and string[i+1] == 'u':
                count +=1
                i+=1
            if count >= 1:
                possiveis = (possiveis * comb(count, vet)) % MOD
            i+=1
        
        count = 0
        if i < len(string) and string[i] == 'n':
            count +=1
            while i < len(string)-1 and string[i+1] == 'n':
                count +=1
                i+=1
            if count > 1:
                possiveis = (possiveis * comb(count, vet)) % MOD
            i+=1
        else:
            i+=1
        
    print(str(possiveis))

main()