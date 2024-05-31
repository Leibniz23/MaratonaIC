def valePasse(n, m, a, b):
    if n >= m:
        if b <= a*m:
            return True
        else:
            return False
    else:
        if b < a*n:
            return True
        else:
            return False
        

def main():
    n, m, a, b = input().split(" ")
    n, m, a, b = int(n), int(m), int(a), int(b)
    passes, unicos = 0,0
    while n > 0:
        if valePasse(n, m, a, b):
            if n >= m:
                passes += (n // m)*b
                n = n % m
            else:
                passes += b
                n = 0
        else:
            unicos += n*a
            n = 0
    
    print(str(passes + unicos))

main()