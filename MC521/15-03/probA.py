def main():
    n = int(input())
    planes = input().split(" ")
    a = 0
    while a < n:
        b = int(planes[a]) - 1
        c = int(planes[b]) - 1
        if int(planes[c]) == int(a) + 1:
            print("YES")
            return
        a += 1
    print("NO")
main()