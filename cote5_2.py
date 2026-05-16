# 카운트 값을 두고 탐색중인 위치에 따라서 +1 해주면 될듯

import sys
input = sys.stdin.readline

h, w = map(int, input().split())

arr = [[0]*(w) for _ in range(h)]

for i in range(h):
    for j in range(w):
        count = 0
        if i > 0:
            count += 1
        if i < h - 1:
            count += 1
        if j > 0:
            count += 1
        if j < w - 1:
            count += 1
            
        arr[i][j] = count
            
for row in arr:
    print(*row)