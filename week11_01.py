# 백준 2110번
import sys
input = sys.stdin.readline

n, c = map(int, input().split()) 
houses = [] 

for _ in range(n):
    houses.append(int(input()))

houses.sort() # 집의 위치를 정렬

def count(distance): 
    count = 1
    last_position = houses[0]

    for i in range(1, n):
        if houses[i] - last_position >= distance:
            count += 1
            last_position = houses[i]

    return count

low, high = 0, houses[-1] - houses[0]
result = 0
while low <= high:
    mid = (low + high) // 2
    if count(mid) >= c:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
