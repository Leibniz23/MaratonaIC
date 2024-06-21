def main():
    n = int(input())
    nums = list(map(int, input().split()))
    a = nums[0]
    b = nums[1]
    even = False
    if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
        c = nums[2]
        if (a % 2 == 0 and c % 2 == 0) or (a % 2 != 0 and c % 2 != 0):
            print("2") # indice do b, ele é o diferente
            return
        else:
            print("1")
            return
    elif a % 2 == 0 and b % 2 == 0:
        even = True
    else:
        even = False

    for i in range(2, n):
        if even:
            if nums[i] % 2 != 0:
                print(str(i+1))
                return
        else:
            if nums[i] % 2 == 0:
                print(str(i+1))
                return

main()