import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = []

for i in range(n):
    li.append(input().rstrip())

# dp[i][j] = (i, j)에서 끝나는 정사각형의 최대 크기
dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if li[i][j] == '1': # 현재 탐색하는 곳이 채워져 있다면
            
            if i == 0 or j == 0: # 첫 번째 행 또는 첫 번째 열인 경우
                dp[i][j] = 1 # 첫 번째 테두리에서는 1이 최대 크기니깐
                
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 
                # 왼쪽, 위뿐만이 아니라 대각선도 고려해야함!

answer = 0

# 정사각형 중에 가장 큰값을 추출
for i in range(n):
    for j in range(m):
        answer = max(answer, dp[i][j])
        
print(answer**2)
