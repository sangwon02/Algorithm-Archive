import sys
input = sys.stdin.readline

def power(n, k):
    if k == 0:
        return 1
    
    half = power(n, k // 2)
    
    # 지수가 짝수라면
    if k % 2 == 0:
        return (half * half) % 1000000007
    # 지수가 홀수라면
    else:
        return (half * half * n) % 1000000007

n, k = map(int, input().split())
print(power(n, k))