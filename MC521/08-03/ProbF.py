def main():
    n = input()
    lenght = len(n)
    n = int(n)
    if lenght == 1:
        print(n)
        return
    digit = 1
    sum = 0
    for i in range(lenght-1):
        sum += 9*(10**i) * digit
        digit += 1

    sum += ((n+1) - 10**(digit-1))*digit
    print(sum)

main()