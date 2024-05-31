def rook(moves):
    r1, c1, r2, c2 = moves
    count = 0
    if r1 != r2:
        count += 1
    if c1 != c2:
        count += 1
        
    return count # Pelo menos 1
    
def bishop(moves):
    r1, c1, r2, c2 = moves
    count = 0
    if (r1+c1) % 2 == (r2+c2) % 2:
        if abs(r1-r2) == abs(c1-c2):
            count = 1
        else:
            count = 2
        
    return count # Pode ser 0
    
def king(moves):
    r1, c1, r2, c2 = moves
    
    return max(abs(r1-r2),abs(c1-c2)) # Pelo menos 1

def main():
    moves = list(map(int, input().split()))
    r, b, k = rook(moves), bishop(moves), king(moves)
    print(r, b, k)

main()