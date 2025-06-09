#lab4
def nearest_zero_distance(street):
    n = len(street)
    result = [0] * n
    last_zero = -float('inf')

    for i in range(n):
        if street[i] == 0:
            last_zero = i
        result[i] = i - last_zero

    last_zero = float('inf')
    for i in reversed(range(n)):
        if street[i] == 0:
            last_zero = i
        result[i] = min(result[i], last_zero - i)

    return result

n = int(input())
arr = list(map(int, input().split()))
print(' '.join(map(str, nearest_zero_distance(arr))))
