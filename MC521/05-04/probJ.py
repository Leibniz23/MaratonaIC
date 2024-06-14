def main():
    t = int(input())
    for _ in range(t):
        a, b, c = input().split()
        a, b, c = int(a), int(b), int(c)
        div = (a+b+c) // 9
        if a < div or b < div or c < div:
            print("NO")
        elif (a + b + c) % 9 == 0:
            print("YES")
        else:
            print("NO")

main()