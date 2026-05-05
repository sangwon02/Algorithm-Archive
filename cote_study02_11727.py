import sys
input = sys.stdin.readline


n = int(input())
dp = [0] * (n+1) # dp 리스트 생성
dp[1] = 1 # 첫번째 값

if n >= 2: # n이 2보다 크면 값을 넣어줌
    dp[2] = 3
    
for i in range(3, n + 1): # 점화식을 통해 dp 리스트 채워줌
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007
    
print(dp[n])