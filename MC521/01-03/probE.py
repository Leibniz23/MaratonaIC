def main():
    n = int(input())
    t = input().split()
    a_list, b_list, c_list = [], [], []
    a, b, c = 0, 0, 0
    for i in range(n):
        if t[i] == '1':
            a += 1
            a_list.append(i+1)

        elif t[i] == '2':
            b += 1
            b_list.append(i+1)

        elif t[i] == '3':
            c += 1
            c_list.append(i+1)

    m = min(a, b, c)
    print(str(m))
    for i in range(m):
        a, b, c = a_list.pop(), b_list.pop(), c_list.pop()
        print(a, b, c)

main()