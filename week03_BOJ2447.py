import sys
input = sys.stdin.readline

def dp(n):
    if n == 1:
        return ["***", "* *", "***"]
    
    else:
        prev = dp(n//3)
        new = []
        for i in range(len(prev)):
            new.append(prev[i]*3)
        for i in range(len(prev)):
            new.append(prev[i] + " "*(len(prev[i])) + prev[i])
        for i in range(len(prev)):
            new.append(prev[i]*3)
        return new


n = int(input())
n = n//3
result = dp(n)

for line in result:
    print(line)