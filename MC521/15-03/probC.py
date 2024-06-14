def main():
    n_q = int(input())
    while n_q > 0:
        n = int(input())
        result = [1] * n
        query = input().split()
        for i in range(n):
            atual = int(query[i]) - 1
            while atual != i:
                atual = int(query[atual]) - 1
                result[i] += 1
        n_q -= 1
        for i in range(n):
            print(str(result[i]) + " ", end="")
        print() # para tirar uma linha
        
main()