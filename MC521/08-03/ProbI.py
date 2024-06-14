def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        if m % 2 == 0:
            print(m // 2)
        else:
            print((m // 2) + 1)
main()