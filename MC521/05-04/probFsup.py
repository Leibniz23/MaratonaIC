MAX_H = 2*(10**5)

def solved(n, x, vec_a, h) -> int:
    total = x
    for i in range(n):
        ai = int(vec_a[i])
        if ai < h:
            dif = h - ai
            total -= dif
        if total < 0: # a altura é muito grande
            return total

    return total

def findH(n, x, vec_a, h) -> int:
    max = MAX_H
    min = 0
    h = (max + min) // 2
    best = 0
    while max > min:
        result = solved(n, x, vec_a, h)
        if result < 0: # h é muito grande, faltou x
            h = h // 2
            max = h
        elif result > 0: # h é muito pequeno, sobrou x
            min = h
            h = h + (h // 2)
            max = h
        else:
            best = h
            break

        if h > best and (result > 0 and result <= x):
            best = h
    
    return best

    
        
def main():
    t = int(input())
    for _ in range(t):
        n, x = input().split()
        n, x = int(n), int(x)
        vec_a = input().split()
        h = findH(n, x, vec_a, MAX_H)
        print(h)

main()