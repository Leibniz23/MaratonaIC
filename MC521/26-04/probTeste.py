def check(mid, array, n, K):
    count = 0
    _sum = 0
    for i in range(n):
        if array[i] > mid:
            return False
        _sum += array[i]
        if _sum > mid:
            count += 1
            _sum = array[i]
    count += 1
    if count <= K:
        return True
    return False

def solve(array, n, K):
    _max = max(array)
    start = _max
    end = sum(array)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if check(mid, array, n, K):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

n, k = map(int, input().split())
arr = list(map(int, input().split()))
resultado = solve(arr, n, k)
print(f"A soma máxima dos subarrays com {k} divisões é minimizada para {resultado}.")