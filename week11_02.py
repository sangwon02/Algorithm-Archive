# 백준 2343번
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = list(map(int, input().split()))

low, high = max(li), sum(li)
result = 0

while low <= high:
    mid = (low + high) // 2
    count = 1
    current_sum = 0

    for x in li:
        if current_sum + x > mid:
            count += 1
            current_sum = x
        else:
            current_sum += x

    if count <= m:
        result = mid
        high = mid - 1
    else:
        low = mid + 1

print(result)