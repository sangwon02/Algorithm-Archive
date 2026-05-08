n = int(input())
li = list(map(int, input().split()))

li.sort()
res = 0

for i in range(n):
    res += sum(li[:i+1])

print(res)