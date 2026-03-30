import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [[0] * M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        arr[i][j] = row[j]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    sum = 0
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            sum += arr[i][j]
    print(sum)