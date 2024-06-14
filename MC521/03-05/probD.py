def main():
    t = int(input())
    for _ in range(t):
        n, x = list(map(int,input().split()))
        array = list(map(int, input().split()))
        array.sort(reverse=True) # decrescente
        soma = array[0]
        valor = array[0]
        if valor < x:
            print("0")
            continue

        count = 1
        while count <= n - 1:
            soma += array[count]
            valor = (soma) / (count+1)
            if valor >= x:
                count += 1
            else:
                break

        print(count)

main()