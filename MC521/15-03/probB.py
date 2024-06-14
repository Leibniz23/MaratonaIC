def main():
    n, q = input().split()
    n, q = int(n), int(q)
    conj = set()
    for _ in range(q):
        entrada = input().split()
        if entrada[0] == "=":
            conj.add(entrada[1])
            conj.add(entrada[2])
        elif entrada[0] == "?":
            if (entrada[1] in conj) and (entrada[2] in conj):
                print("yes")
            else:
                if entrada[1] == entrada[2]:
                    print("yes")
                else:
                    print("no")

main()