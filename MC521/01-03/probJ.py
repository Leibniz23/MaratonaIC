def countingSort(sin):
    """ Counting sort adaptado para 3 elementos diferentes"""
    
    n = len(sin)
    sout = [0]*n
    c = [0, 0, 0]
    for i in range(n):
        k = int(sin[i]) - 1
        c[k] += 1

    c[0] = c[0] - 1
    c[1] = c[1] + c[0]
    c[2] = c[2] + c[1]

    for j in range(n-1, -1, -1):
        k = int(sin[j]) - 1
        sout[c[k]] = sin[j]
        c[k] -= 1

    return sout

def main():
    sin = input().split("+")
    sout = countingSort(sin)
    print("+".join(sout))

main()