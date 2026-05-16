import sys
input = sys.stdin.readline
from collections import deque

s = input().rstrip()
queue = deque(s)
n = int(input())

for _ in range(n):
    queue.popleft()
    queue.pop()
    
s = "".join(queue)
print(s)