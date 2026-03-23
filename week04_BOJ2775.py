import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    
    li = [[0] * (n) for _ in range(k+1)]
    
    for i in range(0, n):
        li[0][i] = i + 1
    
    for i in range(1, k+1):
        for j in range(0, n):
            if j == 0:
                li[i][j] = 1
            else:
                li[i][j] = li[i-1][j] + li[i][j-1]
    
    print(li[k][n-1])