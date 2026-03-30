import sys
input = sys.stdin.readline

L1, L2 = map(int, input().split())
K1, K2 = map(int, input().split())

li1 = []
li2 = []

for _ in range(K1+K2):
    Y, X, V = map(int, input().split())
    if Y == 1:
        li1.append(V)
    elif Y == 2:
        li2.append(V)
        
li = set(li1) & set(li2)
res = len(li)
print(res)