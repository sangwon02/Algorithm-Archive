import sys
input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

for i in range(n//2):
    li[i*2], li[i*2+1] = li[i*2+1], li[i*2]
    
print(*li)
