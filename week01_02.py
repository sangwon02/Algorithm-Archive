import sys
input = sys.stdin.readline

n = int(input())

st = [""] * (n+1) 

st[1] = "1"

for i in range(2, n+1):
    st[i] = st[i-1] + " " + str(i) + " " + st[i-1]

print(st[n])