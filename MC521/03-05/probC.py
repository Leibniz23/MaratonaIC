from _heapq import *  # Disponível em Lib/heapq.py

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)

def update_heap(sum_heap, a_list, b_list, n):
    value, i = sum_heap[0]
    if i == 0:
        if a_list[i+1] == -1:
            value -= b_list[i]
    elif i == n-1:
        if a_list[i-1] == -1:
            value -= b_list[i]

    else:
        if a_list[i-1] == -1:
            value -= b_list[i]
        if a_list[i+1] == -1:
            value -= b_list[i]
    
    sum_heap[0] = [value, i]
    _siftup(sum_heap, 0)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
        sum_heap = []
        for i in range(n):
            if i == 0 or i == n-1:
                heappush(sum_heap, [a_list[i] + b_list[i], i])
            else:
                heappush(sum_heap, [a_list[i] + 2*b_list[i], i])
        time = 0
        while len(sum_heap) > 0: # da ultima vez ele vai tirar o ultimo que falta
            value, i = heappop(sum_heap)
            time += value
            a_list[i] = -1
            if len(sum_heap) == 0:
                break
            update_heap(sum_heap, a_list, b_list, n) # vai olhar o valor do topo no heap e ver se ele deve ser mudado (se os vizinhos são -1), se forem muda o elemento

        print(str(time))
#talvez funcione com lista ligada
main()

