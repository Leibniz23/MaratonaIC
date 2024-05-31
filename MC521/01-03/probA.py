def ordem(str1, str2, n):
    """ Recebe 2 strings e o tamanho delas e retorna 0 se as strings tem mesma ordem, 
    -1 se a primeira vem antes e 1 se a segunda vem antes """
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(n):
        if ord(str1[i]) < ord(str2[i]):
            return -1
        elif ord(str2[i]) < ord(str1[i]):
            return 1
    return 0

def main():
    # Entradas
    str1 = input()
    str2 = input()

    # Quantificando pontuação
    n = len(str1)
    result = ordem(str1, str2, n)
    print(str(result))

main()