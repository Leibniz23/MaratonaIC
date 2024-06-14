def main():
    n, m = input().split(" ")
    n, m = int(n), int(m)
    flag = True
    for i in range(n):
        if i % 2 == 0:
            print(m * "#")
        else:
            if flag:
                print(((m-1) * ".") + "#")
                flag = False
            else:
                print("#" + ((m-1) * "."))
                flag = True

main()