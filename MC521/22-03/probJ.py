def buscar(a, b, c):
    sol = []
    for x in range(-21, 22):
        if x*x <= c:
            for y in range(x+1,101):
                if x*x + y*y <= c:
                    for z in range(y+1, 101):
                        if (x*x + y*y + z*z == c) and (x*y*z == b) and (x+y+z == a):
                            sol = [x, y, z]
                            return sol
    return sol

def main():
    casos = int(input())
    for _ in range(casos):
        a, b, c = input().split(" ")
        a, b, c = int(a), int(b), int(c)
        sol = buscar(a,b,c)
        if len(sol) == 0:
            print("No solution.")
        else:
            print(str(sol[0]) + " " + str(sol[1]) + " " + str(sol[2]))
            
main()  