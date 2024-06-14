def main():
    num = int(input())
    string = input()
    n, z = 0, 0
    for i in range(num):
        if string[i] == "n":
            n += 1
        elif string[i] == "z":
            z += 1
    for i in range(n):
        print("1 ", end="")
    for j in range(z):
        print("0 ", end="")


main()