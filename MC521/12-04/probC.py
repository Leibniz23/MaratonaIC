def main():
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    best = 1
    count = 1
    while i < n-1:
        if a[i] <= a[i+1]:
            count +=1
            if count > best:
                best = count
        else:
            count = 1
            
        i+=1
    print(str(best))

main()